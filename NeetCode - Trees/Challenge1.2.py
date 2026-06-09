class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal1(self, root: TreeNode) -> list[int]:
        if not root:
            return []

        stack = [root]
        res = []
        visited = {root}

        while stack:
            node = stack[-1]

            if node.left and node.left not in visited:
                stack.append(node.left)
                visited.add(node.left)
            else:
                temp = stack.pop()
                res.append(temp.val)

                if temp.right and temp.right not in visited:
                    stack.append(temp.right)
                    visited.add(temp.right)

        return res
    
    def inorderTraversal2(self, root: TreeNode) -> list[int]:
        stack = []
        curr = root
        res = []

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right

        return res


node6 = TreeNode(6)
node7 = TreeNode(7)
node4 = TreeNode(4)
node5 = TreeNode(5)
node2 = TreeNode(2, node4, node5)
node3 = TreeNode(3, node6, node7)
node1 = TreeNode(1, node2, node3)

sol = Solution()
print(sol.inorderTraversal2(node1))