class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        minSum = nums[0]
        currMinSum = nums[0]
        maxSum = nums[0]
        currMaxSum = nums[0]
        totalSum = sum(nums)

        for i in range(1, len(nums)):
            if currMaxSum < 0:
                currMaxSum = 0
            currMaxSum += nums[i]
            maxSum = max(maxSum, currMaxSum)

            if currMinSum + nums[i] > nums[i]:
                currMinSum = 0
            currMinSum += nums[i]  
            minSum = min(minSum, currMinSum)

        minSum = minSum if minSum != totalSum else maxSum
        return max(maxSum, totalSum - minSum)

sol = Solution()
nums=[-2,-3,-1]
print(sol.maxSubarraySumCircular(nums))