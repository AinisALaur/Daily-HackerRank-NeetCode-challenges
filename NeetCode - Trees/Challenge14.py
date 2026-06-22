class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            n = len(q)
            level = []

            for i in range(n):
                popped = q.popleft()
                
                if popped.left:
                    q.append(popped.left)
                if popped.right:
                    q.append(popped.right)

                if i == n - 1:
                    res.append(popped.val)
        
        return res