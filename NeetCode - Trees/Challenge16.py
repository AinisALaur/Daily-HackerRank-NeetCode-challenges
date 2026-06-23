# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:        
        self.goodNodeCount = 0

        def dfs(node, currMax):
            if not node:
                return

            if node.val >= currMax:
                self.goodNodeCount += 1

            dfs(node.left, max(node.val, currMax))
            dfs(node.right, max(node.val, currMax))

        dfs(root, root.val)

        return self.goodNodeCount


node5 = TreeNode(-1)
node3 = TreeNode(3)
node4 = TreeNode(4)
node2 = TreeNode(2, node3, node4)
node1 = TreeNode(1,node2, node5)

sol = Solution()
print(sol.goodNodes(node1))