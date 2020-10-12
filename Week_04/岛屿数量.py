#注意判断边界条件的时候不要越界
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        count = 0
        n, m = len(grid), len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    self.dfs(i, j, n, m, grid)
                    count += 1
        return count

    def dfs(self, i, j, n, m, grid):
        if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == "0":
            return

        grid[i][j] = "0"
        self.dfs(i + 1, j, n, m, grid)
        self.dfs(i - 1, j, n, m, grid)
        self.dfs(i, j - 1, n, m, grid)
        self.dfs(i, j + 1, n, m, grid) 
