class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, arr):
            if i == len(nums):
                res.append(arr.copy())
                return

            arr.append(nums[i])
            backtrack(i + 1, arr)

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            
            arr.pop()
            backtrack(i + 1, arr)
        
        backtrack(0, [])
        return res
            