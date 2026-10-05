class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # transpose of the matrix
        #   rows -> cols
        # reverse the columns of the transpose
        # [i, j] <-> [j, i]

        rows = len(matrix)
        cols = len(matrix[0])

        for r in range(rows):
            for c in range(r, cols):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        
        for row in range(rows):
            matrix[row].reverse()