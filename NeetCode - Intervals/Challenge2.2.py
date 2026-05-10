class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted(intervals, key = lambda i : i.start)
        ends = sorted(intervals, key = lambda i : i.end)
        size = len(intervals)

        rooms = 0
        maxRooms = 0

        i = 0
        j = 0

        while i < size and j < size:
            if starts[i].start < ends[j].end:
                rooms += 1
                maxRooms = max(maxRooms, rooms)
                i += 1
            else:
                rooms -= 1
                j += 1
        
        return maxRooms