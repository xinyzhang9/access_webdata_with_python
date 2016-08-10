# You are given a m x n 2D grid initialized with these three possible values.

# -1 - A wall or an obstacle.
# 0 - A gate.
# INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
# Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

# For example, given the 2D grid:
# INF  -1  0  INF
# INF INF INF  -1
# INF  -1 INF  -1
#   0  -1 INF INF
# After running your function, the 2D grid should be:
#   3  -1   0   1
#   2   2   1  -1
#   1  -1   2  -1
#   0  -1   3   4

class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return
        m,n = len(rooms),len(rooms[0])
        def bfs(rooms,i,j):
            queue = [(i,j)]
            dist = 0
            visited = set()
            visited.add((i,j))
            while queue:
                size = len(queue)
                for x in range(size):
                    row,col = queue.pop(0)
                    rooms[row][col] = min(rooms[row][col],dist)
                    # up
                    if row-1 >= 0 and rooms[row-1][col] > 0 and (row-1,col) not in visited:
                        queue.append((row-1,col))
                        visited.add((row-1,col))
                    # left
                    if col-1 >= 0 and rooms[row][col-1] > 0 and (row,col-1) not in visited:
                        queue.append((row,col-1))
                        visited.add((row,col-1))
                    # down
                    if row < m-1 and rooms[row+1][col] > 0 and (row+1,col) not in visited:
                        queue.append((row+1,col))
                        visited.add((row+1,col))
                    # right
                    if col < n-1 and rooms[row][col+1] > 0 and (row,col+1) not in visited:
                        queue.append((row,col+1))
                        visited.add((row,col+1))
                dist += 1
            
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    bfs(rooms,i,j)
    
        