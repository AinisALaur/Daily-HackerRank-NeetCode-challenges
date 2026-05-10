
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        size = len(intervals)
        if size == 0:
            return 0
        
        intervals.sort(key = lambda i : i.start)
        rooms = 1

        finished = set()
        for i in range(size - 1):
            r = i + 1
            pair = -1
            while r < size:
                if intervals[i].end <= intervals[r].start and r not in finished:
                    pair = r
                    break
                r += 1

            if pair != -1:
                finished.add(pair)
            else:
                rooms += 1
        
        return rooms
    