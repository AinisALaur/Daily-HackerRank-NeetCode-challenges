class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        counts = {}
        for element in hand:
            if element not in counts:
                counts[element] = 1
            else:
                counts[element] += 1
        
        def getMin():
            minVal = 1000
            for key, val in counts.items():
                if val > 0 and key < minVal:
                    minVal = key
            return minVal

        size = 0
        while size < len(hand):
            currentSize = 0
            current = getMin()
            while currentSize < groupSize:
                if current not in counts or counts[current] <= 0:
                    return False
                currentSize += 1
                counts[current] -= 1
                current += 1
            size += groupSize
        
        return True
    
sol = Solution()
hand = [1,2,4,2,3,5,3,4]
groupSize = 4
print(sol.isNStraightHand(hand, groupSize))
