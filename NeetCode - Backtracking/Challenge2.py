class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        def backtrack(i, result):
            if i == len(nums):
                res.append(result.copy())
                return

            result.append(nums[i])
            backtrack(i + 1, result)

            result.pop()
            backtrack(i + 1, result)

        backtrack(0, [])
        return res

sol = Solution()
print(sol.subsets([1,2,3]))