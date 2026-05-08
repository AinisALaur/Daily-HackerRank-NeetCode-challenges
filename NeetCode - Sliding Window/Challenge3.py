class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        maxLength = 0
        chars = set()

        while j < len(s):
            while s[j] in chars:
                chars.remove(s[i])
                i += 1

            chars.add(s[j])
            maxLength = max(maxLength, len(chars))
            j += 1

        return maxLength
    

sol = Solution()
s = "zxyzxyz"
print(sol.lengthOfLongestSubstring(s))
