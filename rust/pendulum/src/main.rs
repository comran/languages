extern crate nalgebra as na;
extern crate rand;

use na::Vector2;
use rand::distributions::{Distribution, Uniform};
use std::thread;

////////////////////////////////////////////////////////////////////////////////
// Constants

const GRAVITY_ACC_M_PER_S_PER_S: f64 = 9.81;
const LENGTH_M: f64 = 1.0;
const MASS_KG: f64 = 1.0;
const TIMESTEP_S: f64 = 1.0 / 1000.0;
const CONVERGENCE_TOLERANCE_RADIANS: f64 = 1.0 * std::f64::consts::PI / 180.0;
const STABILITY_TIME_S: f64 = 5.0;
const RANDOM_WALK_NUMBER_OF_SIMS: i32 = 500;

////////////////////////////////////////////////////////////////////////////////

fn pendulum_step(
    state: Vector2<f64>,
    damping_factor_kg_s: f64,
    length_m: f64,
    mass_kg: f64,
) -> Vector2<f64> {
    let angle_position_delta: f64 = state[1];
    let angle_velocity_delta: f64 = (-damping_factor_kg_s * mass_kg) * state[1]
        + (-GRAVITY_ACC_M_PER_S_PER_S / length_m) * state[0].sin();

    let state_delta = Vector2::new(angle_position_delta, angle_velocity_delta);

    return state_delta;
}

fn pendulum_simulation(
    initial_state: Vector2<f64>,
    timestep_s: f64,
    damping_factor_kg_s: f64,
    length_m: f64,
    mass_kg: f64,
) -> f64 {
    let mut state = initial_state;
    let mut current_time = 0.0;
    let mut stability_timer_start: f64 = f64::NAN;

    loop {
        let state_delta = pendulum_step(state, damping_factor_kg_s, length_m, mass_kg);

        state += state_delta * timestep_s;
        current_time += timestep_s;

        if state[0] < CONVERGENCE_TOLERANCE_RADIANS {
            if stability_timer_start.is_nan() {
                stability_timer_start = current_time;
            } else if current_time - stability_timer_start > STABILITY_TIME_S {
                break;
            }
        } else {
            // Tolerance exceeded, so timer should be reset.
            stability_timer_start = f64::NAN;
        }
    }

    return stability_timer_start;
}

fn random_walk_pendulum_tune(number_of_sims: i32) -> Vector2<f64> {
    let damping_factor_distribution = Uniform::from(1.0..5.0);
    let mut rng = rand::thread_rng();
    let mut best_stability_timer_start = f64::NAN;
    let mut best_damping_factor = f64::NAN;
    let initial_state = Vector2::new(std::f64::consts::FRAC_PI_2, 0.0);

    for _ in 0..number_of_sims {
        let damping_factor_sample = damping_factor_distribution.sample(&mut rng) as f64;

        let stability_timer_start = pendulum_simulation(
            initial_state,
            TIMESTEP_S,
            damping_factor_sample,
            LENGTH_M,
            MASS_KG,
        );

        if best_damping_factor.is_nan() || stability_timer_start < best_stability_timer_start {
            best_stability_timer_start = stability_timer_start;
            best_damping_factor = damping_factor_sample;
        }
    }

    let result = Vector2::new(best_damping_factor, best_stability_timer_start);
    return result;
}

fn main() {
    let mut handles = Vec::new();

    // Spawn multiple threads to run simulations.
    for _i in 0..8 {
        let handle = thread::spawn(|| {
            let thread_best_damping_factor = random_walk_pendulum_tune(RANDOM_WALK_NUMBER_OF_SIMS);

            thread_best_damping_factor
        });

        handles.push(handle);
    }

    // Wait for workers to finish, and determine the best result.
    let mut best_damping_pair: Vector2<f64> = Vector2::new(f64::NAN, f64::NAN);
    for handle in handles {
        let handle_best_damping_pair = handle.join().unwrap();

        if best_damping_pair[1].is_nan() || handle_best_damping_pair[1] < best_damping_pair[1] {
            best_damping_pair = handle_best_damping_pair;
        }
    }

    println!("Best damping: {}", best_damping_pair[0]);
}
