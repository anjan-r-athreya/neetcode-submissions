from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # similar to the walls/gates, islands/treasure question:
        # we want to perform bfs simultaneously outward from each rotten fruit

        # initialize #rows #cols queue & visited
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque()
        visited = set()

        # locate the rotten fruits
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append([r, c])
                    visited.add((r, c))
        
        # helper function to check eligibility and move outward
        def addFruit(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in visited or grid[r][c] == 0:
                return
            queue.append([r, c])
            visited.add((r, c))
        
        time = 0

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

                addFruit(r - 1, c)
                addFruit(r + 1, c)
                addFruit(r, c - 1)
                addFruit(r, c + 1)
            time += 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    return -1
        
        return max(0, time - 1)