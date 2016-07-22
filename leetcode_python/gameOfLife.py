# [2nd bit, 1st bit] = [next state, current state]

# - 00  dead (next) <- dead (current)
# - 01  dead (next) <- live (current)  
# - 10  live (next) <- dead (current)  
# - 11  live (next) <- live (current) 
# In the beginning, every cell is either 00 or 01.
# Notice that 1st state is independent of 2nd state.
# Imagine all cells are instantly changing from the 1st to the 2nd state, at the same time.
# Let's count # of neighbors from 1st state and set 2nd state bit.
# Since every 2nd state is by default dead, no need to consider transition 01 -> 00.
# In the end, delete every cell's 1st state by doing >> 1.
# For each cell's 1st bit, check the 8 pixels around itself, and set the cell's 2nd bit.

# Transition 01 -> 11: when board == 1 and lives >= 2 && lives <= 3.
# Transition 00 -> 10: when board == 0 and lives == 3.
# To get the current state, simply do

# board[i][j] & 1
# To get the next state, simply do

# board[i][j] >> 1

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if board == []:
            return
        m,n = len(board),len(board[0])
        for i in range(m):
            for j in range(n):
                lives = self.countNeighbors(board,m,n,i,j)
                if board[i][j] == 1 and lives >= 2 and lives <= 3:
                    board[i][j] = 3
                if board[i][j] == 0 and lives == 3:
                    board[i][j] = 2
        
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1
    
    def countNeighbors(self,board,m,n,i,j):
        lives = 0
        for x in range(max(0,i-1),min(i+2,m)):
            for y in range(max(0,j-1),min(j+2,n)):
                lives += board[x][y] & 1
        lives -= board[i][j] & 1
        return lives
        