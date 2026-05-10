import heapq
class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        meetings.sort()
        available = [i for i in range(n)]
        used = [] # (end, room)
        count = [0] * n

        for meeting in meetings:
            start = meeting[0]
            end = meeting[1]

            while used and start >= used[0][0]:
                _, room = heapq.heappop(used)
                heapq.heappush(available, room)
            
            if not available:
                end_time, room = heapq.heappop(used)
                end = end_time + (end - start)
                heapq.heappush(available, room)
            
            room = heapq.heappop(available)
            heapq.heappush(used, (end, room))
            count[room] += 1
            
        return count.index(max(count))

sol = Solution()
meetings = [[1,20],[2,10],[3,5],[6,8],[4,9]]
n = 3
print(sol.mostBooked(n, meetings))