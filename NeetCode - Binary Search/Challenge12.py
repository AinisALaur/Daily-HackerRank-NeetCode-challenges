class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        l = max(nums)
        h = sum(nums)

        res = h

        while l <= h:
            m = l + (h - l) // 2

            subArrays = 1
            currentSum = 0
            for i in range(len(nums)):
                if currentSum + nums[i] <= m:
                    currentSum += nums[i]
                else:
                    subArrays += 1
                    currentSum = nums[i]

            if subArrays <= k:
                res = m
                h = m - 1
            else:
                l = m + 1

        return res
    
sol = Solution()
nums = [1,0,2,3,5]
k = 4
print(sol.splitArray(nums, k))
