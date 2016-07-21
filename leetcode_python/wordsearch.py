# Given a 2D board and a word, find if the word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

# For example,
# Given board =

# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# word = "ABCCED", -> returns true,
# word = "SEE", -> returns true,
# word = "ABCB", -> returns false.


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if board == []:
            return 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.helper(board,word[1:],i,j):
                        return True
                    
        return False
        
    def helper(self,board,word,r,c):
        if word == '':
            return True
        tmp = board[r][c]
        board[r][c] = '#'
        
        if r-1 >= 0 and board[r-1][c] == word[0]:
            if self.helper(board,word[1:],r-1,c):
                return True
                
        if r+1 < len(board) and board[r+1][c] == word[0]:
            if self.helper(board,word[1:],r+1,c):
                return True
        if c-1 >=0 and board[r][c-1] == word[0]:
            if self.helper(board,word[1:],r,c-1):
                return True
        if c+1 < len(board[0]) and board[r][c+1] == word[0]:
            if self.helper(board,word[1:],r,c+1):
                return True
                
        board[r][c] = tmp # recover board[r][c] if no results found
        return False