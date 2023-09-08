class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def dfs(node):
    if node == None:
        return
    dfs(node.left)
    dfs(node.right)
    return

root = TreeNode(0)
one = TreeNode(1)
two = TreeNode(2)

root.left = one
root.right = two

dfs(root)