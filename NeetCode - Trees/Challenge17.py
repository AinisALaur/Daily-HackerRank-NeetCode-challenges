class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:        
        def dfs(node, min, max):
            if not node:
                return True
            
            if not min < node.val < max:
                return False

            return dfs(node.left, min, node.val) and dfs(node.right, node.val, max)

        return dfs(root, float("-inf"), float("inf"))
    
node8 = TreeNode(8)
node10 = TreeNode(10, node8)
node9 = TreeNode(9, None, node10)
node4 = TreeNode(4)
node5 = TreeNode(5,node4, node9)

sol = Solution()
print(sol.isValidBST(node5))
    