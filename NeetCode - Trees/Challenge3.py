class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> list[int]:
        stack = []
        curr = root
        res = []

        while curr or stack:
            while curr:
                res.append(curr.val)
                stack.append(curr)
                curr = curr.right
            
            curr = stack.pop()
            curr = curr.left

        return res[::-1]

node6 = TreeNode(6)
node7 = TreeNode(7)
node4 = TreeNode(4)
node5 = TreeNode(5)
node2 = TreeNode(2, node4, node5)
node3 = TreeNode(3, node6, node7)
node1 = TreeNode(1, node2, node3)

sol = Solution()
print(sol.postorderTraversal(node1))