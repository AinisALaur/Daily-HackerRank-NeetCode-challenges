class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if not root:
            return None

        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        if root.val == target and not root.left and not root.right:
            return None

        return root

    def printTree(self, root):
        if not root:
            return

        print(root.val)
        self.printTree(root.left)
        self.printTree(root.right)
    

node4444 = TreeNode(4)
node444 = TreeNode(4, node4444)
node44 = TreeNode(4, node444)
node4 = TreeNode(4, node44)
node3 = TreeNode(3, node4)
node2 = TreeNode(2, node3)
node1 = TreeNode(1, node2)

sol = Solution()
sol.removeLeafNodes(node1, 4)
sol.printTree(node1)
