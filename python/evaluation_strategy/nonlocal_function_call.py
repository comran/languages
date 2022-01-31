def func1():
    x = 5

    def func2():
        x = 2

    func2()
    return x


def func3():
    x = 5

    def func4():
        nonlocal x
        x = 2

    func4()
    return x

################################################################################
# Test cases.


assert func1() == 5
assert func3() == 2
