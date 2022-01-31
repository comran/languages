# LC 314

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def verticalOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    lsts = {}
    bfs = [(0, root)]
    min_n = 0
    max_n = 0

    while bfs:
        n, x = bfs.pop(0)
        if x is None:
            continue

        if n not in lsts:
            lsts[n] = []
            min_n = min(min_n, n)
            max_n = max(max_n, n)

        lsts[n].append(x.val)
        bfs.append((n - 1, x.left))
        bfs.append((n + 1, x.right))

    out = []
    for n in range(min_n, max_n + 1):
        out.append(lsts[n])

    return out


################################################################################
# Test cases.
tst = TreeNode(
    val=3,
    left=TreeNode(
        val=9,
        left=TreeNode(val=4),
        right=TreeNode(val=0),
    ),
    right=TreeNode(
        val=8,
        left=TreeNode(val=1),
        right=TreeNode(val=7),
    )
)

assert verticalOrder(tst) == [[4], [9], [3, 0, 1], [8], [7]]
