class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: TreeNode) -> int:
        
        def dfs(node):
            if not node:
                return [0, 0]

            left = dfs(node.left)
            right = dfs(node.right)

            withRoot = node.val + left[1] + right[1]
            withoutRoot = max(left) + max(right)

            return [withRoot, withoutRoot]

        return max(dfs(root))
        

node2 = TreeNode(2)
node4 = TreeNode(4)
node5 = TreeNode(5)

node3 = TreeNode(3, node4, node2)
node22 = TreeNode(2, node3, node5)
node1 = TreeNode(1, None, node22)

sol = Solution()
print(sol.rob(node1))