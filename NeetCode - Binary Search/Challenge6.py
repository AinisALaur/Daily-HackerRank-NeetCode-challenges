import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        low = 1
        high = max(piles)
        res = high

        while low <= high:
            k = low + (high - low) // 2

            time = 0
            for pile in piles:
                time += math.ceil(pile / k)

            if time > h:
                low = k + 1

            if time <= h:
                res = k
                high = k - 1

        return res
    
sol = Solution()
piles = [1,1,1,999999999]
h = 10
print(sol.minEatingSpeed(piles, h))