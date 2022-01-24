# LC 312

from typing import List


def burst_balloons(nums: List[int]) -> int:
    nums = [1] + nums + [1]
    nums_len = len(nums)
    dp = [[0] * nums_len for _ in range(nums_len)]

    for i in range(nums_len - 3, -1, -1):
        for j in range(i + 2, nums_len):
            dp[i][j] = max(
                [
                    dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j]
                    for k in range(i + 1, j)
                ]
            )

    return dp[0][-1]


################################################################################
# Test cases.
assert burst_balloons([3, 1, 5, 8]) == 167
assert burst_balloons([1, 5]) == 10
