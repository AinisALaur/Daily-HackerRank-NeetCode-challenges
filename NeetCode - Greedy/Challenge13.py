class Solution:
    def checkValidString(self, s: str) -> bool:
        maxLeft = 0
        minLeft = 0

        for char in s:
            if char == '(':
                maxLeft += 1
                minLeft += 1
            elif char == ')':
                maxLeft -= 1
                minLeft -= 1
            else:
                maxLeft += 1
                minLeft -= 1

            if maxLeft < 0:
                return False

            if minLeft < 0:
                minLeft = 0    
        
        return minLeft == 0
    
sol = Solution()
s = "((**)"
print(sol.checkValidString(s))