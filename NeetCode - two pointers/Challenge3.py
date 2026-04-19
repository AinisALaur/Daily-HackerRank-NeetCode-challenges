class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPallindrome(start, end):
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1

            return True
        
        i = 0
        j = len(s) - 1
        
        while i < j:   
            if s[i] != s[j]:
                return isPallindrome(i + 1, j) or isPallindrome(i, j - 1)

            i += 1
            j -= 1

        return True


sol = Solution()
print(sol.validPalindrome("abdda"))