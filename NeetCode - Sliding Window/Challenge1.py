class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        mapping = {}

        for dx, dy in enumerate(nums):
            if dy not in mapping:
                mapping[dy] = dx
            else:
                if dx - mapping[dy] <= k:
                    return True
                else:
                    mapping[dy] = dx
        
        return False