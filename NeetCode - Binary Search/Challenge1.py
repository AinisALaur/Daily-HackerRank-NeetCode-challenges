class Solution:
    def search(self, nums: list[int], target: int) -> int:
        i = 0
        j = len(nums) - 1

        while i <= j:
            mid = int(i + (j - i) / 2)

            if nums[mid] < target:
                i = mid + 1
            
            elif nums[mid] > target:
                j = mid - 1
            
            else:
                return mid
        
        return -1

sol = Solution()
nums = [-1,0,2,4,6,8]
target = 4
print(sol.search(nums, target))