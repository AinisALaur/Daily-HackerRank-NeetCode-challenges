class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        l = 0
        r = len(arr) - 1

        while r - l + 1 > k:
            if abs(x - arr[l]) > abs(x - arr[r]):
                l += 1
            else:
                r -= 1
        
        return arr[l: r + 1]
    
sol = Solution()
arr = [1,2,3,4,5,6,7,8,9]
x = 8
k = 3
print(sol.findClosestElements(arr, k, x))