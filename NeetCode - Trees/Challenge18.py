# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int):
        stack = []
        curr = root
        res = []

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            if len(res) == k:
                return res[-1]

            curr = curr.right

        return res[-1]



node2 = TreeNode(2)
node4 = TreeNode(4)
node6 = TreeNode(6)
node8 = TreeNode(8)

node7 = TreeNode(7, node6, node8)
node3 = TreeNode(3, node2, node4)
node5 = TreeNode(5, node3, node7)

sol = Solution()
print(sol.kthSmallest(node5, 8))

