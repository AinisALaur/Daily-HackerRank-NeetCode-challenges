class Solution:
    def minWindow(self, s: str, t: str) -> str:
        size1 = len(s)
        size2 = len(t)

        if size1 < size2:
            return ""
        
        counts1 = {}

        for char in t:
            if char not in counts1:
                counts1[char] = 1
            else:
                counts1[char] += 1

        counts2 = {}

        def checkCounts():
            for key, val in counts1.items():
                if key not in counts2 or counts2[key] < val:
                    return False

            return True

        l = 0

        ans = ""
        for r in range(len(s)):
            if s[r] not in counts2:
                counts2[s[r]] = 1
            else:
                counts2[s[r]] += 1

            if checkCounts():
                while checkCounts() and l <= r:
                    counts2[s[l]] -= 1
                    l += 1
                
                subAns = s[l - 1: r + 1]
                if len(subAns) < len(ans) or ans == "":
                    ans = subAns
        
        return ans
    

sol = Solution()
s="ab"
t="a"
print(sol.minWindow(s, t))