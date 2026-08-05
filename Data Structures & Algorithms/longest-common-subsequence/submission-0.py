class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # if same char: take the min of surrounding and add one
        # if different: take the max of surrounding

        n = len(text1)
        m = len(text2)

        matrix = [[0] * (m+1) for i in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                if text1[i-1] == text2[j-1]: 
                    matrix[i][j] = matrix[i-1][j-1] + 1
                else:
                    matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
        
        return matrix[n][m]