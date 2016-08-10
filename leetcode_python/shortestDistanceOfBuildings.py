import sys
# You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

# Each 0 marks an empty land which you can pass by freely.
# Each 1 marks a building which you cannot pass through.
# Each 2 marks an obstacle which you cannot pass through.
# For example, given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2):

# 1 - 0 - 2 - 0 - 1
# |   |   |   |   |
# 0 - 0 - 0 - 0 - 0
# |   |   |   |   |
# 0 - 0 - 1 - 0 - 0
# The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal. So return 7.

# Note:
# There will be at least one building. If it is not possible to build such house according to the above rules, return -1.

class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return -1
        nrow, ncol = len(grid), len(grid[0])
        dists, visited_nums, building_num = {}, {}, 0
        min_dist = float("inf")
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        for i, row in enumerate(grid):
            for j, ele in enumerate(row):
                if ele == 1:
                    building_num += 1
                    queue = collections.deque()
                    queue.append((i, j, 0))
                    visited = {}
                    while queue:
                        x, y, dist = queue.popleft()
                        for di,dj in dirs:
                            xx,yy = x+di,y+dj
                            if xx >= 0 and xx < nrow and yy >=0 and yy < ncol and grid[xx][yy] == 0 and (xx,yy) not in visited:
                                dists[(xx,yy)] = dists.get((xx,yy),0) + dist + 1
                                visited_nums[(xx,yy)] = visited_nums.get((xx,yy),0) + 1
                                visited[(xx,yy)] = True
                                queue.append((xx,yy,dist+1))
        
        for x, y in dists:
            if dists[(x, y)] < min_dist and visited_nums[(x, y)] == building_num:
                min_dist = dists[(x, y)]
        
        if min_dist == float("inf"):
            return -1
        return min_dist

s = Solution()
grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
print s.shortestDistance(grid)