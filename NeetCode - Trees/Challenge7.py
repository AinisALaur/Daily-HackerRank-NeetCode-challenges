class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> int:
        self.ans = True
        def dfs(curr):
            if not curr:
                return 0

            left = dfs(curr.left)
            right = dfs(curr.right)

            if abs(left - right) > 1:
                self.ans = False

            return 1 + max(left, right)

        dfs(root)

        return self.ans


node5 = TreeNode(5)
node4 = TreeNode(4, node5)
node3 = TreeNode(3, node4)
node2 = TreeNode(2)
node1 = TreeNode(1, node2, node3)

sol = Solution()
print(sol.isBalanced(node1))