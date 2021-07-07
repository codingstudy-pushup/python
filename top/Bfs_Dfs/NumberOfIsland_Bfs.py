import collections
from typing import List


class Solution:
    def solve(self, grid):
        if not grid: return 0
        m = len(grid)
        n = len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.bfs(grid, i, j)
                    count += 1
        return count

    def bfs(self, grid, i, j):
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        q = collections.deque([(i, j)])
        while q:
            x, y = q.popleft()
            for dir in dirs:
                x1 = x + dir[0]
                y1 = y + dir[1]
                if 0 <= x1 < len(grid) and 0 <= y1 < len(grid[0]) and grid[x1][y1] == '1':
                    q.append((x1, y1))
                    grid[x1][y1] = 'X'

if __name__ == "__main__":
    print(Solution().solve([['1', '1', '0', '0', '1'],
                            ['1', '1', '0', '0', '0'],
                            ['1', '1', '0', '0', '0'],
                            ['0', '0', '0', '1', '1']]))
