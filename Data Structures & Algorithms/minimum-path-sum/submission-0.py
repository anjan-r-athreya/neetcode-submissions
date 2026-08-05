class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        matrix = [[0] * m for i in range(n)]

        for i in range(m):
            if i == 0: matrix[0][0] = grid[0][0]
            else: matrix[0][i] = grid[0][i] + matrix[0][i - 1]

        for i in range(1, n):
            matrix[i][0] = grid[i][0] + matrix[i - 1][0]
        
        for i in range(1, n):
            for j in range(1, m):
                matrix[i][j] = grid[i][j] + min(matrix[i-1][j], matrix[i][j-1])
        
        return matrix[n-1][m-1]