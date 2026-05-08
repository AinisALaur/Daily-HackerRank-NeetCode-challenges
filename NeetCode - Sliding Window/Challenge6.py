class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        i = 0
        sum = 0
        minLength = len(nums)
        found = False

        for j in range(len(nums)):
            sum += nums[j]

            while sum >= target:
                found = True
                minLength = min(minLength, j - i  + 1)
                sum -= nums[i]
                i += 1
        
        if found:
            return minLength
        return 0
    
sol = Solution()
nums = [1,2,3,4]
target = 10
print(sol.minSubArrayLen(target, nums))