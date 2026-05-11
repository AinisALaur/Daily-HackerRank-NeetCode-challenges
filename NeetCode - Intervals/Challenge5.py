class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            if res[-1][1] >= intervals[i][0]:
                res[-1] = [min(res[-1][0], intervals[i][0]), max(res[-1][1], intervals[i][1])]
            else:
                res.append([intervals[i][0], intervals[i][1]])
        return res
    
sol = Solution()
intervals = [[1,3],[1,5],[6,7]]
print(sol.merge(intervals))