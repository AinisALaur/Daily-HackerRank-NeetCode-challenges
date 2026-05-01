class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        res = high


        while low <= high:
            mid = low + (high - low ) // 2

            d = 1
            total = 0
            for weight in weights:
                if total + weight <= mid:
                    total += weight
                else:
                    total = weight
                    d += 1

            if d <= days:
                res = mid
                high = mid - 1
            else:
                low = mid + 1

        return res
                

sol = Solution()
weights = [1,5,4,4,2,3]
days = 3
print(sol.shipWithinDays(weights, days))
