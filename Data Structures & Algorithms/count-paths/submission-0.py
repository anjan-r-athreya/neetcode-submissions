class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # initialize a mxn matrix full of zeroes
        matrix = [[0] * m for i in range(n)]

        for i in range(m):
            matrix[0][i] = 1
        
        for i in range(n):
            matrix[i][0] = 1

        for i in range(1, n):
            for j in range(1, m):
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
        
        return matrix[n-1][m-1]