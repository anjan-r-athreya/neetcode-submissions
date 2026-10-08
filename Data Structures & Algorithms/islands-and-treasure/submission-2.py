from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque()
        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append([r, c])
                    visited.add((r, c))

        def addLand(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in visited or grid[r][c] == -1:
                return
            queue.append([r, c])
            visited.add((r, c))

        distance = 0

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = distance

                addLand(r + 1, c)
                addLand(r - 1, c)
                addLand(r, c + 1)
                addLand(r, c - 1)
            distance += 1