class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.bestPath = float("-inf")

        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            left = max(0, left)
            right = max(0, right)

            path = node.val + left + right
            self.bestPath = max(self.bestPath, path)
            return node.val + max(left, right)
        dfs(root)
        return self.bestPath