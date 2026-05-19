from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        D, R = deque(), deque()

        for i, c in enumerate(senate):
            if c == "R":
                R.append(i)
            else:
                D.append(i)

        
        while R and D:
            Dval = D.popleft()
            Rval = R.popleft()

            if Rval < Dval:
                R.append(Rval + len(senate))
            else:
                D.append(Dval + len(senate))
        
        return "Radiant" if R else "Dire"

sol = Solution()
senate = "RRDDD"
print(sol.predictPartyVictory(senate))