class Solution:
    def canJump(self, nums: list[int]) -> bool:
        goal = len(nums) - 1
        i = len(nums) - 2

        while i >= 0:
            if nums[i] + i >= goal:
                goal = i

            i -= 1
        
        return goal == 0
    
sol = Solution()
nums = [1, 3, 1, 3, 0, 1, 0]
print(sol.canJump(nums))