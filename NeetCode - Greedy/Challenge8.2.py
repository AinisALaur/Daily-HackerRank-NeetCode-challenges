class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        diff = [gas[i] - cost[i] for i in range(len(gas))]

        total = 0
        res = 0
        for i in range(len(gas)):
            total += diff[i]
            if total < 0:
                total = 0
                res = i + 1
                
        return res
    
sol = Solution()
gas = [1,2,3,4]
cost = [2,2,4,1]
print(sol.canCompleteCircuit(gas, cost))