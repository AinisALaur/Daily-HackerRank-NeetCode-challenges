class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        
        def backtrack(i, curr, arr):
            if curr == target:
                res.append(arr.copy())
                return
            
            if curr > target or i >= len(candidates):
                return
            
            arr.append(candidates[i])
            backtrack(i + 1, curr + candidates[i], arr)
            arr.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            backtrack(i + 1, curr, arr)
        
        backtrack(0, 0, [])
        return res