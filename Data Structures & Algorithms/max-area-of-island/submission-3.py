class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(row, col):
            # return 1 + dfs(x, x)
            # base case isn't when we reach a 0 node because that'll never happen
            grid[row][col] = 0 # mark visited
            size = 1

            if row - 1 > -1 and grid[row - 1][col] == 1: size += dfs(row - 1, col)
            if row + 1 < rows and grid[row + 1][col] == 1: size += dfs(row + 1, col)
            if col - 1 > -1 and grid[row][col - 1] == 1: size += dfs(row, col - 1)
            if col + 1 < cols and grid[row][col + 1] == 1: size += dfs(row, col + 1)

            return size

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))
        
        return max_area