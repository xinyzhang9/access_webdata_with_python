class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # cannot pass last test case!
        # if not board:
        #     return
        # m,n = len(board),len(board[0])
        # def check(board,i,j):
        #     if i < 0 or i > m-1 or j < 0 or j > n-1:
        #         return
        #     if board[i][j] == 'O':
        #         board[i][j] = '#'
        #         check(board,i-1,j)
        #         check(board,i+1,j)
        #         check(board,i,j-1)
        #         check(board,i,j+1)
        
        # for i in range(m):
        #     if board[i][0] == 'O':
        #         check(board,i,0)
        #     if board[i][n-1] == 'O':
        #         check(board,i,n-1)
        # for j in range(n):
        #     if board[0][j] == 'O':
        #         check(board,0,j)
        #     if board[m-1][j] == 'O':
        #         check(board,m-1,j)
        # for i in range(m):
        #     for j in range(n):
        #         if board[i][j] == 'O':
        #             board[i][j] = 'X'
        #         if board[i][j] == '#':
        #             board[i][j] = 'O'

        if not any(board): return
        m, n = len(board), len(board[0])
        save = [ij for k in range(m+n) for ij in ((0, k), (m-1, k), (k, 0), (k, n-1))]
        while save:
            i, j = save.pop()
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = 'S'
                save += (i, j-1), (i, j+1), (i-1, j), (i+1, j)
        for row in board:
            for i, c in enumerate(row):
                row[i] = 'XO'[c == 'S']
                
                
        