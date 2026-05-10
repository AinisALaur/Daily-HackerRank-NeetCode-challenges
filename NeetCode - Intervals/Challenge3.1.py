class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        meetings.sort(key = lambda i : i[0])
        rooms = {} # we will only save end times for each meeting

        for meeting in meetings:
            start = meeting[0]
            end = meeting[1]

            bestRoom = -1
            added = False
            shortestWait = 500000
            for i in range(n):
                if i not in rooms:
                    rooms[i] = [end]
                    added = True
                    break

                if start >= rooms[i][-1]:
                    rooms[i].append(end)
                    added = True
                    break

                waitTime = rooms[i][-1] - start
                if waitTime < shortestWait:
                    shortestWait = waitTime
                    bestRoom = i

            if added:
                continue

            duration = end - start     
            rooms[bestRoom].append(rooms[bestRoom][-1] + duration) 

        maxRoom = 0
        for key, val in rooms.items():
            if len(rooms[key]) > len(rooms[maxRoom]):
                maxRoom = key
        
        return maxRoom

sol = Solution()
meetings = [[1,20],[2,10],[3,5],[6,8],[4,9]]
n = 3
print(sol.mostBooked(n, meetings))