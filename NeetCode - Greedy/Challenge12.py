class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        lastPos = {}

        for i in range(len(s)):
            lastPos[s[i]] = i

        res = []
        end, size = 0, 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, lastPos[c])

            if i == end:
                res.append(size)
                size = 0

        return res
    
sol = Solution()
s = "xyxxyzbzbbisl"
print(sol.partitionLabels(s))