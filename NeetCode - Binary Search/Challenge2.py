class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        l = 0
        h = len(nums) - 1

        while l <= h:
            mid = int(l + (h - l) / 2)

            if nums[mid] < target:
                l = mid + 1
            
            elif nums[mid] > target:
                h = mid - 1
            else:
                return mid

        return l
    
sol = Solution()
nums = [-1,0,2,4,6,8]
target = 5
print(sol.searchInsert(nums, target))