class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        res = []
        def preorder(root):
            if not root:
                return

            res.append(root.val)
            preorder(root.left)
            preorder(root.right)

        preorder(root)
        return res
            


node6 = TreeNode(6)
node7 = TreeNode(7)
node4 = TreeNode(4)
node5 = TreeNode(5)
node2 = TreeNode(2, node4, node5)
node3 = TreeNode(3, node6, node7)
node1 = TreeNode(1, node2, node3)

sol = Solution()
print(sol.preorderTraversal(node1))