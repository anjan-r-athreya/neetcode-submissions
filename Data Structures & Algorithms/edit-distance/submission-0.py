class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)

        matrix = [[0] * (n1+1) for i in range(n2+1)]

        # matrix where the horizontal is word1
        # and the vertical is word2

        # initialize matrix sentinal rows
        for i in range(1, n1+1):
            if word1[i-1] != word2[0]:
                matrix[1][i] = matrix[1][i-1] + 1
            else:
                matrix[1][i] = matrix[1][i-1]
        
        for i in range(1, n2+1):
            if word2[i-1] != word1[0]:
                matrix [i][1] = matrix[i-1][1] + 1
            else:
                matrix[i][1] = matrix[i-1][1]

        for i in range(2, n2 + 1):
            for j in range(2, n1 + 1):
                if word1[j-1] == word2[i-1]:
                    matrix[i][j] = matrix[i-1][j-1]
                else:
                    matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1
        
        return matrix[n2][n1]



