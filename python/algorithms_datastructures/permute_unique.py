# LC 47

from typing import List


def permute_unique(nums: List[int]) -> List[List[int]]:
    def backtrack(tmp, size):
        if len(tmp) == size:
            ans.append(tmp[:])
        else:
            for i in range(size):
                if visited[i] or (i > 0 and nums[i] == nums[i-1] and not visited[i-1]):
                    continue

                visited[i] = True
                backtrack(tmp + [nums[i]], size)
                visited[i] = False

    ans = []
    visited = [False] * len(nums)
    nums.sort()
    backtrack([], len(nums))
    return ans


################################################################################
# Test cases.

cases = [
    (
        ([1, 1, 2],),
        [[1, 1, 2], [1, 2, 1], [2, 1, 1]],
    ),
    (
        ([1, 2, 3],),
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]],
    ),
]


def check(a, b):
    a = [tuple(sorted(x)) for x in a]
    b = [tuple(sorted(x)) for x in b]
    a.sort()
    b.sort()
    assert a == b


for case in cases:
    check(permute_unique(*case[0]), case[1])
