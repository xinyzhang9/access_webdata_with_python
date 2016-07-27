class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n < 1:
            return list()
        res = [[1] * n for q in range(n)]
        visited = [[0] * n for q in range(n)]
        visited[0][0] = 1
        dirs = [[0,1],[1,0],[0,-1],[-1,0]] # right,down,left,up
        i,j,i_pre,j_pre = 0,0,0,0
        cnt = 0
        k = 2
        while k <= n*n:       
            i,j = i+dirs[cnt % 4][0],j+dirs[cnt % 4][1]

            if i < 0 or j < 0 or i>n-1 or j>n-1:
                cnt += 1
                i,j = i_pre,j_pre
            else:
                if visited[i][j] == 0:
                    print 'set res[',i,'][',j,'] = ',k
                    res[i][j] = k
                    visited[i][j] = 1
                    k+= 1
                    i_pre,j_pre = i,j
        print res               
        return res

s = Solution()
s.generateMatrix(3)

# res = [[0] * n for q in range(n)]
        # i,j,di,dj = 0,0,0,1
        # for k in xrange(n*n):
        #     res[i][j] = k+1
        #     if res[(i+di)%n][(j+dj)%n]:
        #         di,dj = dj,-di
        #     i += di
        #     j += dj
        # return res

# https://discuss.leetcode.com/topic/19130/4-9-lines-python-solutions