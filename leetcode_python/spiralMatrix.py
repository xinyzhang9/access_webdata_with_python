class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
            return []

        numRows,numCols = len(matrix),len(matrix[0])
        visited = [[False for x in range(numCols)] for y in range(numRows)]
        i,j = 0,0
        res = [matrix[0][0]]
        visited[0][0] = True
        directions = [[0,1],[1,0],[0,-1],[-1,0]] #right,down,left,up
        direct_cnt = 0
        i_pre,j_pre = 0,0
        if numCols == 1:
            direct_cnt += 1
        for x in range(numRows * numCols):
            direction = directions[direct_cnt % 4]
            i,j = i+direction[0],j+direction[1]        
            while i >=0 and i<numRows and j>=0 and j<numCols and visited[i][j] is False:
                visited[i][j] = True
                res.append(matrix[i][j])
                i_pre,j_pre = i,j
                i,j = i+direction[0],j+direction[1]

            if i <0 or i >= numRows or j < 0 or j > numCols:
                i,j = i_pre,j_pre
                direct_cnt += 1
        return res
            
                
s = Solution()
matrix = [[1,2],[6,3],[5,4]]
s.spiralOrder(matrix)
        