class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        l = 0
        r = len(arr) - k

        while l < r:
            m = l + (r - l) // 2
            print(m)

            if abs(arr[m] - x) > abs(arr[m + k] - x):
                l = m + 1
            else:
                r = m
        
        return arr[l: l + k]
    
sol = Solution()
arr = [1,2,3,4,5,6,7,8,9]
x = 3
k = 8
print(sol.findClosestElements(arr, k, x))