class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        maxDepth = 0
        curr = root
        stack = []
        depth = 0
        
        while stack or curr:
            while curr:
                depth += 1
                maxDepth = max(maxDepth, depth)
                stack.append((curr, depth))
                curr = curr.left

            curr, depth = stack.pop()
            curr = curr.right

        return maxDepth

node6 = TreeNode(6)
node7 = TreeNode(7)
node4 = TreeNode(4)
node5 = TreeNode(5)
node2 = TreeNode(2, node4, node5)
node3 = TreeNode(3, node6, node7)
node1 = TreeNode(1, node2, node3)

# node4 = TreeNode(4)
# node3 = TreeNode(3, node4)s
# node2 = TreeNode(2)
# node1 = TreeNode(1, node2, node3)


sol = Solution()
print(sol.maxDepth(node1))