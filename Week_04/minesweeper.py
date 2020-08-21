class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board

        m = len(board)
        n = len(board[0])
        surrounds = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1))

        def check(i, j):
            num = 0
            for x, y in surrounds:
                if 0 <= x + i < m and 0 <= y + j < n and board[x+i][y+j] == 'M':
                    num += 1
            return num

        def dfs(i, j):
            num = check(i, j)
            if num:
                board[i][j] = str(num)
            else:
                board[i][j] = 'B'
                for x, y in surrounds:
                    if 0 <= x + i < m and 0 <= y + j < n and board[x+i][y+j] == 'E':
                        dfs(x + i, y + j)

        dfs(click[0], click[1])
        return board


