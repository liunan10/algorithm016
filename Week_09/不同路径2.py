class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * m for _ in range(n)]
        if obstacleGrid[0][0] == 1: return 0
        dp[0][0] = 1
        for i in range(1, n):
            dp[i][0] = 0 if obstacleGrid[i][0] else dp[i - 1][0]

        for j in range(1, m):
            dp[0][j] = 0 if obstacleGrid[0][j] else dp[0][j - 1]

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = 0 if obstacleGrid[i][j] else dp[i - 1][j] + dp[i][j - 1]
                     
        return dp[n - 1][m - 1]
