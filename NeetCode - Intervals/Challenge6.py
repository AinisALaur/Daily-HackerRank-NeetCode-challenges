class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort()

        nonOverlaping = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] < nonOverlaping[-1][1]:
                if intervals[i][1] <= nonOverlaping[-1][1]:
                    nonOverlaping[-1] = intervals[i]
            else:
                nonOverlaping.append(intervals[i])
        
        return len(intervals) - len(nonOverlaping)

sol = Solution()
intervals = [[1,2],[2,4],[1,4]]
print(sol.eraseOverlapIntervals(intervals))
