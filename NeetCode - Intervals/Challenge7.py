import heapq
class Solution:
    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        intervals.sort()
        res, i = {}, 0
        minHeap = []
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minHeap, (r - l + 1, r))
                i += 1

            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            
            res[q] = minHeap[0][0] if minHeap else -1

        
        return [res[q] for q in queries]  

sol = Solution()
intervals = [[6,6],[5,5],[10,10],[3,6],[9,9],[7,7],[2,10],[5,5],[3,7],[10,10]]
queries = [1,8,9,1,8,3,9,3,10,1]
print(sol.minInterval(intervals, queries))