class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(num, arr):
            if len(arr) == k:
                res.append(arr.copy())
                return

            if num > n:
                return

            arr.append(num)
            backtrack(num + 1, arr)
            arr.pop()
            backtrack(num + 1, arr)
        
        backtrack(1, [])
        return res