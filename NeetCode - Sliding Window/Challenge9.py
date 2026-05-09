import collections
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        dq = collections.deque()
        l = r = 0
        res = []

        while r < len(nums):
            while len(dq) > 0 and nums[dq[-1]] < nums[r]:
                dq.pop()
            dq.append(r)

            if l > dq[0]:
                dq.popleft()

            if r - l + 1 == k:
                res.append(nums[dq[0]])
                l += 1

            r += 1

        return res
    
sol = Solution()
nums = [1,2,1,0,4,2,6]
k = 3
print(sol.maxSlidingWindow(nums, k))