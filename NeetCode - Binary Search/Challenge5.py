class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        l = 0
        h = rows * cols - 1

        while l <= h:
            mid = int(l + (h - l) / 2)

            midY, midX = mid // cols, mid % cols
            if matrix[midY][midX] < target:
                l = mid + 1

            elif matrix[midY][midX] > target:
                h = mid - 1

            else:
                return True

        return False   
    
sol = Solution()
matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
target = 10
print(sol.searchMatrix(matrix, target))