class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder_recursive(root):
    ans = []

    def preorder(root):
        if not root:
            return

        nonlocal ans
        ans.append(root.val)
        preorder(root.left)
        preorder(root.right)

    preorder(root)
    return ans


def postorder_recursive(root):
    ans = []

    def postorder(root):
        if not root:
            return

        nonlocal ans
        postorder(root.left)
        postorder(root.right)
        ans.append(root.val)

    postorder(root)
    return ans


def inorder_recursive(root):
    ans = []

    def inorder(root):
        if not root:
            return

        nonlocal ans
        inorder(root.left)
        ans.append(root.val)
        inorder(root.right)

    inorder(root)
    return ans


def preorder_iterative(root):
    ans, stack = [], [root]

    while stack:
        node = stack.pop()
        if node:
            ans.append(node.val)
            stack.append(node.right)
            stack.append(node.left)

    return ans


def postorder_iterative(root):
    ans, stack1, stack2 = [], [root], []

    while stack1:
        node = stack1.pop()
        if node:
            stack2.append(node)
            stack1.append(node.left)
            stack1.append(node.right)

    while stack2:
        node = stack2.pop()
        ans.append(node.val)

    return ans


def inorder_iterative(root):
    ans, stack = [], []

    while root or stack:
        if root:
            stack.append(root)
            root = root.left
        else:
            node = stack.pop()
            ans.append(node.val)
            root = node.right

    return ans
