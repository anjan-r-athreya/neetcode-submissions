class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # middle is middle of middle row
        # matrix[int(len(matrix)) / 2][int(len(matrix[0])) / 2]

        n = len(matrix)
        m = len(matrix[0])

        left = matrix[0][0]
        right = matrix[n-1][m-1]

        l = 0
        r = n-1
        ROW = -1

        while l <= r:
            row = int((r+l) / 2)
            
            if matrix[row][0] <= target and matrix[row][m-1] >= target:
                ROW = row
                break
            elif target < matrix[row][0]:
                r = row - 1
            elif target > matrix[row][m - 1]:
                l = row + 1
        
        if ROW == -1:
            return False
        
        l = 0
        r = m - 1

        while l <= r:
            mid = int((r+l) / 2)

            if target == matrix[ROW][mid]:
                return True
            elif target < matrix[ROW][mid]:
                r = mid - 1
            elif target > matrix[ROW][mid]:
                l = mid + 1
        
        return False