# https://leetcode.com/problems/minimum-path-sum/
class Solution(object):
    # Time complexity:  O(M*N)
    # Space complexity: O(M*N)
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]: return 0

        rows, cols = len(grid), len(grid[0])

        dp = [[0] * cols for _ in range(rows)]
        dp[0][0] = grid[0][0]

        for i in range(1, rows):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        for j in range(1, cols):
            dp[0][j] = dp[0][j-1] + grid[0][j]

        for i in range(1, rows):
            for j in range(1, cols):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        return dp[rows-1][cols-1]
