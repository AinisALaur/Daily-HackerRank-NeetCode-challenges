# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        curr1 = p
        curr2 = q
        stack1 = []
        stack2 = []

        while (stack1 or curr1) or (stack2 or curr2):
            while curr1 or curr2:
                if curr1 and not curr2:
                    return False
                
                if not curr1 and curr2:
                    return False
                
                if curr1.val != curr2.val:
                    return False
                
                stack1.append(curr1)
                stack2.append(curr2)
                curr1 = curr1.left
                curr2 = curr2.left

            curr1 = stack1.pop()
            curr2 = stack2.pop()

            curr1 = curr1.right
            curr2 = curr2.right

        return True

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        curr = root
        stack = []

        while curr or stack:
            while curr:
                if curr.val == subRoot.val:
                    if self.isSameTree(curr, subRoot):
                        return True
                
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            curr = curr.right

        return False