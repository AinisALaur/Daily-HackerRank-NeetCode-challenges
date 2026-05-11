class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxSum = nums[0]
        currSum = nums[0]

        for i in range(1, len(nums)):
            if currSum < 0:
                currSum = 0
            
            currSum += nums[i]
            maxSum = max(currSum, maxSum)
        
        return maxSum

sol = Solution()
nums = [2,-3,4,-2,2,1,-1,4]
print(sol.maxSubArray(nums))