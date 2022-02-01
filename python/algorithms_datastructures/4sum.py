# LC 18

from typing import List


def fourSum(nums: List[int], target: int) -> List[List[int]]:
    seen, ans = set(), set()

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                last_num = target - nums[i] - nums[j] - nums[k]

                if last_num in seen:  # Verify that the fourth number is in the given list.
                    arr = sorted([nums[i], nums[j], nums[k], last_num])
                    ans.add(tuple(arr))

        seen.add(nums[i])

    return [list(x) for x in ans]


################################################################################
# Test cases.

cases = [
    (
        [1, 0, -1, 0, -2, 2],
        0,
        [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]],
    ),
    (
        [2, 2, 2, 2, 2],
        8,
        [[2, 2, 2, 2]],
    ),
    (
        [0, 0, 0],
        0,
        [],
    ),
]

for A, B, expected in cases:
    result = fourSum(A, B)
    for x in expected:
        assert x in result
        result.remove(x)

    assert len(result) == 0
