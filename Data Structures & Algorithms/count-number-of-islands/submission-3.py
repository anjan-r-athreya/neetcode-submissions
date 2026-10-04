class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs method
        # visits turn land "1" into "0" to mark as visited

        num_islands = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(row, col):
            # when we call dfs, it'll only be on land, so curr will always be a 1
            # after we call dfs in the loop, is when we update num_islands.
            # dfs only purpose is to convert 1 into 0
            nonlocal rows
            nonlocal cols

            grid[row][col] = 0

            if row - 1 > -1 and grid[row - 1][col] == "1": dfs(row - 1, col)
            if row + 1 < rows and grid[row + 1][col] == "1": dfs(row + 1, col)
            if col - 1 > -1 and grid[row][col - 1] == "1": dfs(row, col - 1)
            if col + 1 < cols and grid[row][col + 1] == "1": dfs(row, col + 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r, c)
                    num_islands += 1
        
        return num_islands
