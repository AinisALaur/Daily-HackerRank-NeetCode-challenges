class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1':
            return False
        
        j = 0
        while(True):
            lastZeroIndex = j
            jumpFound = False
            for i in range(maxJump - minJump + 1):
                jumpIndex = j + minJump + i
                if jumpIndex == len(s) - 1:
                    return True

                if s[jumpIndex] == '0' and jumpIndex + minJump <= len(s) - 1:
                    jumpFound = True
                    lastZeroIndex = j + minJump + i
            
            if jumpFound == False:
                return False

            j = lastZeroIndex

            if j >= len(s) - 1:
                return True

sol = Solution()
s = "00111010"
minJump = 3
maxJump = 5
print(sol.canReach(s, minJump, maxJump))