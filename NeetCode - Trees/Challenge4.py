class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def inorderTraversal(self, root: TreeNode) -> list[int]:
        res = []
        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        inorder(root)
        return res

    def invertTree(self, root: TreeNode) -> TreeNode:
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                temp = curr.left
                curr.left = curr.right
                curr.right = temp
                curr = curr.left

            curr = stack.pop()
            curr = curr.right

        return root

node6 = TreeNode(6)
node7 = TreeNode(7)
node4 = TreeNode(4)
node5 = TreeNode(5)
node2 = TreeNode(2, node4, node5)
node3 = TreeNode(3, node6, node7)
node1 = TreeNode(1, node2, node3)

sol = Solution()
root = sol.invertTree(node1)
print(sol.inorderTraversal(node1))