class Node:
    def __init__(self, val, isLeaf, topLeft = None, topRight = None, bottomLeft = None, bottomRight = None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: list[list[int]]) -> Node:
        def dfs(n, x, y):
            allSame = True
            for i in range(n):
                for j in range(n):
                    if grid[x][y] != grid[x + i][y + j]:
                        allSame = False
                        break
            
            if allSame:
                return Node(grid[x][y], True)

            n = n // 2
            topleft = dfs(n, x, y)
            topright = dfs(n, x + n, y)
            bottomleft = dfs(n, x, y + n)
            bottomright = dfs(n, x + n, y + n)

            return Node(0, False, topleft, topright, bottomleft, bottomright)
        return dfs(len(grid), 0, 0)

matrix = [
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1]
]

sol = Solution()
print(sol.construct(matrix))