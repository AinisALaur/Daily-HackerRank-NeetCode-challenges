class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        result = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > target:
                break

            if i > 0 and a == nums[i - 1]:
                continue
            
            for x in range(i + 1, len(nums)):
                l = x + 1
                h = len(nums) - 1

                if x - 1 >= i + 1 and nums[x] == nums[x - 1]:
                    continue

                while l < h:
                    currSum = a + nums[x] + nums[l] + nums[h]

                    if currSum < target:
                        l += 1
                    
                    elif currSum > target:
                        h -= 1
                    
                    else:
                        result.append([a, nums[x], nums[l], nums[h]])
                        l += 1
                        while l < h and nums[l] == nums[l - 1]:
                            l += 1

        return result

                    
sol = Solution()
nums1 = [2, 2, 2, 2, 2] 
nums2 = [1,-1,1,-1,1,-1]
nums3 = [3,2,3,-3,1,0]
nums4 = [-1,0,1,2,-1,-4]
print(sol.fourSum(nums1, 8))
print(sol.fourSum(nums2, 2))
print(sol.fourSum(nums3, 3))
print(sol.fourSum(nums4, -1))