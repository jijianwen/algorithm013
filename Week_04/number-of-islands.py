# https://leetcode.com/problems/number-of-islands/
class Solution(object):
    # Time complexity:  O(M*N)
    # Space complexity: O(M*N)
    iter = 0
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(grid, i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
                return
            self.iter += 1
            grid[i][j] = '0'
            dfs(grid, i + 1, j)
            dfs(grid, i - 1, j)
            dfs(grid, i, j + 1)
            dfs(grid, i, j - 1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                self.iter += 1
                if grid[i][j] == '1':
                    self.iter -= 1
                    count += 1
                    dfs(grid, i, j)

        return count
