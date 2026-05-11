class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        counts = {5: 0, 10: 0, 20: 0}

        for bill in bills:
            change = bill - 5

            while change > 0:
                if change - 10 >= 0 and counts[10] > 0:
                    change -= 10
                    counts[10] -= 1
                
                elif change - 5 >= 0 and counts[5] > 0:
                    change -= 5
                    counts[5] -= 1
                
                else:
                    return False
            
            counts[bill] += 1
        
        return True

sol = Solution()
bills = [5,10,5,5,20]
print(sol.lemonadeChange(bills))