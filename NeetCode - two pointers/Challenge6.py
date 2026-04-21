class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0
        j = 0

        size = len(nums)

        while j < size:
            curr = nums[j]
            while j < size and curr == nums[j]:
                j += 1

            nums[i] = curr
            i += 1

        return i

sol = Solution()
arr = [1, 1, 2, 3, 4]
k = sol.removeDuplicates(arr)
for i in range(k):
    print(arr[i])