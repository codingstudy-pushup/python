class Solution:
    # def __init__(self):
    #     self.dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    m = 0
    n = 0
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def numIslands(self, grid):
        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = 'X'
        for dir in self.dirs:
            self.dfs(grid, i + dir[0], j + dir[1])
        # self.dfs(grid, i + 1, j)
        # self.dfs(grid, i - 1, j)
        # self.dfs(grid, i, j + 1)
        # self.dfs(grid, i, j - 1)


if __name__ == "__main__":
    print(Solution().numIslands([['1', '1', '0', '0', '1'],
                                 ['1', '1', '0', '0', '0'],
                                 ['1', '1', '0', '0', '0'],
                                 ['0', '0', '0', '1', '1']]))
