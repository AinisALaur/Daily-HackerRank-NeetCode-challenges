class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0

        i = 0
        j = len(height) - 1

        maxL = height[i]
        maxR = height[j]

        total = 0

        while i < j:
            if maxL < maxR:
                i += 1
                maxL = max(maxL, height[i])
                total += maxL - height[i] 
            else:
                j -= 1
                maxR = max(maxR, height[j])
                total += maxR - height[j]

        return total

sol = Solution()
height = [0,2,0,3,1,0,1,3,2,1]
print(sol.trap(height))