class Solution:
    def twoPointerReverse(self, start, end, nums : list[int]):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -=1

    def rotate(self, nums: list[int], k: int) -> None:
        k = k % len(nums)
        self.twoPointerReverse(0, len(nums) - 1, nums)
        self.twoPointerReverse(0, k - 1, nums)
        self.twoPointerReverse(k, len(nums) - 1, nums)

sol = Solution()
arr = [1, 2, 3, 4, 5]
k = 7
sol.rotate(arr, k)
print(arr)