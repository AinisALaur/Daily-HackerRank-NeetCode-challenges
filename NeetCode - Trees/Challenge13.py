# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            n = len(q)
            subRes = []
            for i in range(n):
                poped = q.popleft()
                if poped.left:
                    q.append(poped.left)
                
                if poped.right:
                    q.append(poped.right)

                subRes.append(poped.val)
            res.append(subRes)
        
        return res