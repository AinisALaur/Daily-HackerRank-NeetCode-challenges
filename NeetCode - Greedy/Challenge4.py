class Solution:
    def jump(self, nums: list[int]) -> int:
        count = 0
        curr = 0
        while curr < len(nums) - 1:
            count += 1
            indexOfMax = curr + 1

            jump = nums[curr]
            if curr + jump >= len(nums) - 1:
                break

            j = curr + 1
            while j <= curr + jump and j < len(nums):
                if indexOfMax + nums[indexOfMax] <= j + nums[j]:
                    indexOfMax = j

                j += 1
            curr = indexOfMax
        
        return count

sol = Solution()
nums = [2,4,1,1,1,1]
print(sol.jump(nums))