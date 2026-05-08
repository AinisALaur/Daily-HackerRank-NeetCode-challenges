class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}

        i = 0 
        j = 0

        maxLength = 0

        def getMostFrequent():
            mostFrequent = 0
            for key, val in counts.items():
                if val > mostFrequent:
                    mostFrequent = val
            return mostFrequent

        while j < len(s):
            if s[j] not in counts:
                counts[s[j]] = 1
            else:
                counts[s[j]] += 1

            while (j - i + 1) - getMostFrequent() > k:
                counts[s[i]] -= 1
                i += 1

            maxLength = max(maxLength, j - i + 1)
            j += 1
        
        return maxLength
    
sol = Solution()
s = "AABABBA"
k = 1
print(sol.characterReplacement(s, k))