# LC 200
from typing import List


def num_islands(grid: List[List[str]]) -> int:
    count = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "1":
                dfs(grid, i, j)
                count += 1

    return count


def dfs(grid: List[List[str]], i: int, j: int):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != "1":
        return

    grid[i][j] = "#"
    dfs(grid, i+1, j)
    dfs(grid, i-1, j)
    dfs(grid, i, j+1)
    dfs(grid, i, j-1)


################################################################################
# Test cases.

cases = [
    (
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ],
        1,
    ),
    (
        [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ],
        3,
    ),
    (
        [
            ["1", "1", "1"],
            ["0", "1", "0"],
            ["1", "1", "1"]
        ],
        1,
    )
]

for tst, expected in cases:
    assert num_islands(tst) == expected
