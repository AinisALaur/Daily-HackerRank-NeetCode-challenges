class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:

        def canWithStart(start):
            tank = gas[start]
            current = start
            for i in range(1, len(gas)):
                tank -= cost[current]

                if tank < 0:
                    return False

                current = (current + 1) % len(gas)
                tank += gas[current]

            return tank - cost[current] >= 0

        for i in range(len(gas)):
            if canWithStart(i):
                return i
        
        return -1
    
sol = Solution()
gas = [4,5,2,6,5,3]
cost = [3,2,7,3,2,9]
print(sol.canCompleteCircuit(gas, cost))