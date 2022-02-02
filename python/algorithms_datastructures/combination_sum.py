# LC 39

from typing import List


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    def backtrack(tmp, start, end, target):
        if target == 0:
            ans.append(tmp)

        elif target > 0:
            for i in range(start, end):
                backtrack(tmp + [candidates[i]], i,
                          end, target - candidates[i])

    ans = []
    candidates.sort(reverse=True)
    backtrack([], 0, len(candidates), target)
    return ans


################################################################################
# Test cases.

cases = [
    (
        ([2, 3, 6, 7], 7),
        [[7], [3, 2, 2]],
    ),
    (
        ([2, 3, 5], 8),
        [[2, 2, 2, 2], [2, 3, 3], [3, 5]],
    ),
    (
        ([2], 1),
        [],
    )
]


def check(a, b):
    a = [tuple(sorted(x)) for x in a]
    b = [tuple(sorted(x)) for x in b]
    a.sort()
    b.sort()
    assert a == b


for case in cases:
    check(combination_sum(*case[0]), case[1])
