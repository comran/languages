# LC 4

from typing import List


def median_of_two_sorted_arrays(A: List[int], B: List[int]) -> float:
    m, n = len(A), len(B)
    if m > n: A, B, m, n = B, A, n, m  # Enforce that A is the shorter length list.
    if n == 0: raise ValueError

    imin, imax, half_len = 0, m, (m + n + 1) // 2
    while imin <= imax:
        i = (imin + imax) // 2
        j = half_len - i

        if i < m and B[j-1] > A[i]: imin = i + 1  # i is too small, must increase it
        elif i > 0 and A[i-1] > B[j]: imax = i - 1  # i is too big, must decrease it
        else:  # i is perfect
            if i == 0: left_max = B[j-1]
            elif j == 0: left_max = A[i-1]
            else: left_max = max(A[i-1], B[j-1])

            if (m + n) % 2 == 1: return left_max  # (m + n) is odd -> median is composed of one number

            if i == m: right_max = B[j]
            elif j == n: right_max = A[i]
            else: right_max = min(A[i], B[j])

            return (left_max + right_max) / 2.0


################################################################################
# Test cases.

cases = [
    (
        [1, 3],
        [2],
        2.0,
    ),
    (
        [1, 2],
        [3, 4],
        2.5,
    ),
]

for A, B, expected in cases:
    assert median_of_two_sorted_arrays(A, B) == expected
