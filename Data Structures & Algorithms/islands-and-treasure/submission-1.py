from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        
        # first we need to locate all the treasure locations
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0: 
                    queue.append([r, c])
                    visited.add((r,c))
        
        # helper function to add checking conditions before adding a land coordinate
        def addLand(r, c):
            # check if r, c in bounds of grid, if r, c already in visited, if r, c is water
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in visited or grid[r][c] == -1:
                return
            visited.add((r, c))
            queue.append([r, c])
        
        # distance from each treasure
        distance = 0

        # perform the bfs spreading out from each treasure
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = distance

                addLand(r - 1, c)
                addLand(r + 1, c)
                addLand(r, c - 1)
                addLand(r, c + 1)
            
            distance += 1
