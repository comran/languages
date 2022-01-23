# LC 42

from typing import List


def trap(height: List[int]) -> int:
    if len(height) < 3:
        return 0

    i = 1
    j = len(height) - 1

    i_max = height[0]
    j_max = height[-1]

    acc = 0

    while i <= j:
        if height[i] > i_max:
            i_max = height[i]

        if height[j] > j_max:
            j_max = height[j]

        if i_max <= j_max:
            d_acc = i_max - height[i]
            i += 1

        else:
            d_acc = j_max - height[j]
            j -= 1

        acc += d_acc

    return acc


################################################################################
# Test cases.

tst = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
expected = 6

result = trap(tst)
assert result == expected
