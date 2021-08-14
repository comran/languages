function fibonacci_dp(size)
    x = Array{Int64}(undef, size)
    x[1] = 1
    x[2] = 1

    for i = 3:(length(x))
        x[i] = x[i - 1] + x[i - 2]
    end

    x
end

for i in [5 10 20 40]
    println(fibonacci_dp(i))
end
