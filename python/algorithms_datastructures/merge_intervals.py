# LC 56
from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort()

    merged_intervals = []
    open_interval = intervals[0]
    for interval in intervals[1:]:
        if interval[0] > open_interval[1]:
            merged_intervals.append(open_interval)
            open_interval = interval

        elif interval[1] > open_interval[1]:
            open_interval[1] = interval[1]

    merged_intervals.append(open_interval)

    return merged_intervals


################################################################################
# Test cases.

cases = [
    (
        [[1, 3], [2, 6], [8, 10], [15, 18]],
        [[1, 6], [8, 10], [15, 18]],
    ),
    (
        [[1, 4], [2, 3]],
        [[1, 4]],
    )
]

for tst, expected in cases:
    assert merge(tst) == expected
