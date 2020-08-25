class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        x, y, di, ans = 0, 0, 0, 0
        obs = set(map(tuple, obstacles))
        for cmd in commands:
            if cmd == -2:
                di = (di + 3) % 4
            elif cmd == -1:
                di = (di + 1) % 4
            else:
                for k in range(cmd):
                    if (x+dx[di], y+dy[di]) not in obs:
                        x += dx[di]
                        y += dy[di]
                        ans = max(x*x + y*y, ans)

        return ans
