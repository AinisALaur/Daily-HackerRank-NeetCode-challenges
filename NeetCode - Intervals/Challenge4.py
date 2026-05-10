class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        newStart = newInterval[0]
        newEnd = newInterval[1]

        if len(intervals) == 0:
            return [newInterval]

        res = []
        i = 0
        inserted = False

        while i < len(intervals) and inserted == False:
            start = intervals[i][0]
            end = intervals[i][1]

            if newStart >= start and newStart <= end:
                while i < len(intervals):
                    if newEnd >= intervals[i][0] and newEnd <= intervals[i][1]:
                        end = intervals[i][1]
                        inserted = True
                        i += 1
                        break
                    
                    elif newEnd < intervals[i][0]:
                        inserted = True
                        end = newEnd
                        break

                    else:
                        inserted = True
                        end = newEnd

                    i += 1

            if newStart < start:
                start = newStart
                end = newEnd
                while i < len(intervals):
                    if newEnd >= intervals[i][0] and newEnd <= intervals[i][1]:
                        inserted = True
                        end = intervals[i][1]
                        i += 1
                        break
                    
                    elif newEnd < intervals[i][0]:
                        inserted = True
                        break

                    else:
                        inserted = True

                    i += 1
            
            if inserted:
                i -= 1

            res.append([start, end])
            i += 1
        
        while i < len(intervals):
            res.append(intervals[i])
            i += 1

        if inserted == False:
            res.append(newInterval)

        return res
    
sol = Solution()
intervals=[[1,5]]
newInterval=[0, 6]
print(sol.insert(intervals, newInterval))
            


            
            


            
            

        

