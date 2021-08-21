extern crate nalgebra as na;
extern crate rand;

use na::Vector2;
use rand::distributions::{Distribution, Uniform};
use std::thread;

////////////////////////////////////////////////////////////////////////////////
// Constants

// Acceleration due to gravity (m/s/s)
const GRAVITY_ACC_M_PER_S_PER_S: f64 = 9.81;

// Length of the pendulum (meters)
const LENGTH_M: f64 = 1.0;

// Mass of the end of the pendulum (kilograms)
const MASS_KG: f64 = 1.0;

// Discrete timestep to use in simulations (seconds)
const TIMESTEP_S: f64 = 1.0 / 1000.0;

// Angle tolerance to use for determining steady state (radians)
const CONVERGENCE_TOLERANCE_RADIANS: f64 = 1.0 * std::f64::consts::PI / 180.0;

// Time that pendulum is required to spend under the angle tolerance to be declared
// in steady state (seconds)
const STABILITY_TIME_S: f64 = 5.0;

// Number of simulations to run per thread to determine best damping factor
const NUMBER_OF_SIMS_PER_THREAD: i32 = 500;

////////////////////////////////////////////////////////////////////////////////

// Finds the derivative at the current state for a pendulum model.
//
// # Arguments
// * `state` - Vector [angle position, angular velocity] representing pendulum state
// * `damping_factor_kg_s` - Damping factor of the pendulum (kg * s)
// * `length_m` - Pendulum length (meters)
// * `mass_kg` - Pendulum end-mass (kilograms)
//
// # Returns
// * Vector [delta angle position, delta angular velocity] representing the state change
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

// Solves an initial value problem for a pendulum, and ends when steady state is reached.
//
// # Arguments
// * `initial_state` - Vector [angle position, angular velocity] representing initial state
// * `timestep_s` - Discrete time step to use (seconds)
// * `damping_factor_kg_s` - Damping factor of the pendulum (kg * s)
// * `length_m` - Pendulum length (meters)
// * `mass_kg` - Pendulum end-mass (kilograms)
//
// # Returns
// * Float (64 bits) representing time elapsed until steady state
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
                // Position is near steady state, so start the stability timer.
                stability_timer_start = current_time;
            } else if current_time - stability_timer_start > STABILITY_TIME_S {
                // Stability requirements met, so end the sim.
                break;
            }
        } else {
            // Tolerance exceeded, so timer should be reset.
            stability_timer_start = f64::NAN;
        }
    }

    return stability_timer_start;
}

// Runs a certain number of sims with randomized damping factors, and returns the best one.
//
// # Arguments
// * `number_of_sims` - Number of simulations to run
//
// # Returns
// * Vector [best damping factor, damping factor stabilize time] representing the best sim outcome
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
            let thread_best_damping_factor = random_walk_pendulum_tune(NUMBER_OF_SIMS_PER_THREAD);

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
