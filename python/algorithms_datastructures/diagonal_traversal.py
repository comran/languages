def diagonal_traversal_from_bottom_right(m):
    diag_sum = 2 * (len(m) - 1)

    row = len(m) - 1
    col = len(m) - 1

    ret = []

    while row >= 0 and col >= 0:
        ret.append(m[row][col])

        row -= 1
        col += 1

        if row < 0:
            diag_sum -= 1
            col = 0
            row = diag_sum

        elif col >= len(m):
            diag_sum -= 1
            row = len(m) - 1
            col = diag_sum - row

    return ret


################################################################################
# Test cases.

tst = [
    [15, 14, 12, 9],
    [13, 11, 8, 5],
    [10, 7, 4, 2],
    [6, 3, 1, 0],
]

assert diagonal_traversal_from_bottom_right(tst) == list(range(16))
