# LC 78

from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    def backtrack(tmp, start, end):
        ans.append(tmp)

        for i in range(start, end):
            backtrack(tmp + [nums[i]], i+1, end)

    ans = []
    backtrack([], 0, len(nums))
    return ans

################################################################################
# Test cases.


cases = [
    (
        ([1, 2, 3],),
        [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]],
    ),
    (
        ([0],),
        [[], [0]],
    ),
]


def check(a, b):
    a = [tuple(sorted(x)) for x in a]
    b = [tuple(sorted(x)) for x in b]
    a.sort()
    b.sort()
    assert a == b


for case in cases:
    check(subsets(*case[0]), case[1])
