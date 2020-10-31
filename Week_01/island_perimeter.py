class Solution:
    # Time complexity:  O(MN)
    # Space complexity: O(1)
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    cnt = 0
                    for k in range(4):
                        tx = i + dx[k]
                        ty = j + dy[k]
                        if tx < 0 or tx >= len(grid) or ty < 0 or ty >= len(grid[0]) or grid[tx][ty] == 0:
                            cnt = cnt + 1
                    ans = ans + cnt
        return ans
