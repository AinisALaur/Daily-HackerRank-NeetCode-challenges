class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(curr):
            if not curr:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)

            self.res = max(self.res, left + right)
            return max(left, right) + 1

        dfs(root)
        return self.res

node6 = TreeNode(6)
node7 = TreeNode(7)
node4 = TreeNode(4)
node5 = TreeNode(5)
node2 = TreeNode(2, node4, node5)
node3 = TreeNode(3, node6, node7)
node1 = TreeNode(1, node2, node3)

sol = Solution()
print(sol.diameterOfBinaryTree(node1))