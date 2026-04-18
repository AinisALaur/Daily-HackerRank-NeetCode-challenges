class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        size = len(s)

        while i < j:
            if (s[i].isalpha() or s[i].isdigit()) and (s[j].isalpha() or s[j].isdigit()):
                l1 = s[i].lower() if s[i].isalpha() else s[i]
                l2 = s[j].lower() if s[j].isalpha() else s[j]
                
                if l1 != l2:
                    return False

                i += 1
                j -= 1

            while i < size and not (s[i].isalpha() or s[i].isdigit()):
                i += 1
            
            while j >= 0 and not (s[j].isalpha() or s[j].isdigit()):
                j -= 1

        return True
    
sol = Solution()
print(sol.isPalindrome("tab is cat"))