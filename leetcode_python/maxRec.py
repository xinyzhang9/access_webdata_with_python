class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        m,n = len(matrix),len(matrix[0])
        left,right,height = [0]*n,[n]*n,[0]*n
        res = 0
        for i in range(m):
            cur_left,cur_right = 0,n
            
            # height
            for j in range(n):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0
            # left boundary
            for j in range(n):
                if matrix[i][j] == '1':
                    left[j] = max(left[j],cur_left)
                else:
                    left[j] = 0
                    cur_left = j+1
            # right boundary
            for j in reversed(range(n)):
                if matrix[i][j] == '1':
                    right[j] = min(right[j],cur_right)
                else:
                    right[j] = n
                    cur_right = j
            # area
            for j in range(n):
                res = max(res,(right[j]-left[j])*height[j])
            print left
            print right
            print height
            print res
        return res

s = Solution()
matrix = [  "10100",
            "10111",
            "11111",
            "10010"]
s.maximalRectangle(matrix)