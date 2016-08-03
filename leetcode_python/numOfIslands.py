# there is a bug when  111
#                      010
#                      111
# class Solution(object):
#     def numIslands(self, grid):
#         """
#         :type grid: List[List[str]]
#         :rtype: int
#         """
#         def getKeyByValue(dic,i,j):
#             for key,val in dic.iteritems():
#                 if (i,j) in val:
#                     return key
#             return None
        
#         def checkDic(dic,i,j):
#             for val in dic.values():
#                 if (i,j) in val:
#                     return True
#             return False

#         if not grid:
#             return 0
#         dic = dict()
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == "1":
#                     flag = 0
#                     if i-1 >=0 and checkDic(dic,i-1,j):
#                         key = getKeyByValue(dic,i-1,j)
#                         dic[key].append((i,j))
#                         flag = 1
#                     if j-1 >=0 and checkDic(dic,i,j-1):
#                         key = getKeyByValue(dic,i,j-1)
#                         dic[key].append((i,j))
#                         flag = 1
#                     if flag == 0:
#                         dic[(i,j)] = list()
#                         dic[(i,j)].append((i,j))
#         print dic
#         return len(dic)
        
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def merge(grid,i,j):
            if i < 0 or i > len(grid)-1 or j < 0 or j > len(grid[0])-1:
                return
            if grid[i][j] == '1':
                grid[i][j] = '0'
                merge(grid,i-1,j)
                merge(grid,i,j-1)
                merge(grid,i+1,j)
                merge(grid,i,j+1)
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    cnt += 1
                    merge(grid,i,j)
        return cnt        
                    
s = Solution()
grid = ["111","010","111"]
print s.numIslands(grid)