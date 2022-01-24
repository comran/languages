# LC 135

from typing import List


# two pass
def candy_two_pass(ratings: List[int]) -> int:
    n = len(ratings)
    ans = [1] * n

    for i in range(n-1):
        if ratings[i] < ratings[i + 1]:
            ans[i + 1] = 1 + ans[i]

    for i in range(n-2, -1, -1):
        if ratings[i + 1] < ratings[i]:
            ans[i] = max(1 + ans[i + 1], ans[i])

    return sum(ans)


# one pass
def candy_one_pass(ratings: List[int]) -> int:
    ans = 1
    inc = 1
    dec = 1
    n = len(ratings)

    for i in range(1, n):
        prev_ans = ans
        if ratings[i] > ratings[i - 1]:
            # Increasing.
            if i > 1 and ratings[i - 1] < ratings[i - 2]:
                # Previously decreasing.
                inc = 1

            inc += 1
            ans += inc
            dec = 1

        elif ratings[i] < ratings[i - 1]:
            # Decreasing.
            ans += dec
            dec += 1

            if dec > inc:
                # Length of current decreasing sequence exceeds last increasing
                # sequence.
                ans += 1

        else:
            # Neither increasing nor decreasing.
            ans += 1
            inc = 1
            dec = 1

    return ans


################################################################################
# Test cases.
for candy in (candy_one_pass, candy_two_pass):
    assert candy([1, 0, 2]) == 5
    assert candy([1, 2, 2]) == 4
    assert candy([0, 1, 2, 5, 3, 2, 7]) == 15
    assert candy([1, 5, 3, 2, 1]) == 11
    assert candy([1, 6, 4, 3, 2, 1]) == 16
