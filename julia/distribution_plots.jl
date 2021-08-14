using Distributions
using Plots


function plot_distributions()
    uniform_d = Distributions.Uniform(0, 100)
    uniform_x = rand(uniform_d, 100000)

    normal_d = Distributions.truncated(Distributions.Normal(50, 15), 0, 100)
    normal_x = rand(normal_d, 50000)

    weibull_d = Distributions.truncated(Distributions.Weibull(1, 50), 0, 100)
    weibull_x = rand(weibull_d, 50000)

    Plots.histogram(uniform_x, bins=100, title = "Distributions Test", xlabel = "Distribution Location", ylabel = "Count")
    Plots.histogram!(weibull_x, bins=100)
    Plots.histogram!(normal_x, bins=100)
end

plot_distributions()
