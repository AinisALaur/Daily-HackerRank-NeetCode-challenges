class Solution:
    def maxTurbulenceSize(self, arr: list[int]) -> int:
        i = 0
        j = 1
        lastComp = ''
        maxLength = 1
        while j < len(arr):
            if arr[j] > arr[j - 1] and lastComp == 'L':
                i = j - 1

            elif arr[j] < arr[j - 1] and lastComp == 'G':
                i = j - 1
            
            elif arr[j] == arr[j - 1]:
                i = j
                lastComp = ''

            else:
                if arr[j] < arr[j - 1]:
                    lastComp = 'G'
                else:
                    lastComp = 'L'
                maxLength = max(maxLength, j - i + 1)

            j += 1

        return maxLength
    
sol = Solution()
arr = [9,4,2,10,7,8,8,1,9]
print(sol.maxTurbulenceSize(arr))