class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def postorder_dfs(node):
    if not node:
        return
    
    postorder_dfs(node.left)
    postorder_dfs(node.right)
    print(node.val)
    return

root = TreeNode(0)
one = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)
four = TreeNode(4)
five = TreeNode(5)
six = TreeNode(6)

root.left = one
root.right = two
root.left.left = three
root.left.right = four
root.right.left = five
root.right.right = six

postorder_dfs(root)