class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        good = set()

        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
            
            for i, v in enumerate(triplet):
                if v == target[i]:
                    good.add(i)
        
        return len(good) == 3

sol = Solution()
triplets = [[2,5,6],[1,4,4],[5,7,5]]
target = [5,4,6]
print(sol.mergeTriplets(triplets, target))