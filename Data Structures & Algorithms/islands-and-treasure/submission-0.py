from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # bfs
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        queue = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append([r, c])
                    visit.add((r, c))

        def addRoom(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == -1 or (r, c) in visit:
                return

            visit.add((r, c))
            queue.append([r, c])

        distance = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = distance

                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)
            
            distance += 1