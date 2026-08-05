class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        reverse = s[::-1]

        matrix = [[0] * (n+1) for i in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, n+1):
                if s[i-1] == reverse[j-1]: 
                    matrix[i][j] = matrix[i-1][j-1] + 1
                else:
                    matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
        
        return matrix[n][n]