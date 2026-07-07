class Solution:
    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:
        res = []

        def backtrack(i, currSum, arr):
            if currSum == target:
                res.append(arr.copy())
                return
            
            if currSum > target or i >= len(nums):
                return
            
            arr.append(nums[i])
            backtrack(i, currSum + nums[i], arr)
            arr.pop()
            backtrack(i + 1, currSum, arr)
        
        backtrack(0, 0, [])
        return res