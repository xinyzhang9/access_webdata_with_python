class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
# brutal force solution
#         r = set()
#         c = set()
#         m,n = len(matrix),len(matrix[0])
#         for i in range(m):
#         	for j in range(n):
#         		if image[i][j] == 1:
#         			r.add(i)
#         			c.add(j)
#         return len(r)*len(c)


# s = Solution()
# matrix = [[0,0,1,0],[0,1,1,0],[0,1,0,0]]
# print s.minArea(matrix,0,2)


# binary search solution
class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        def search(lo,hi,check):
            while lo < hi:
                mid = lo + (hi-lo)/2
                if check(mid):
                    hi = mid
                else:
                    lo = mid+1
            return lo
            
        top = search(0,x,lambda x: '1' in image[x])
        bottom = search(x,len(image),lambda x: '1' not in image[x])
        left = search(0,y,lambda y: any(row[y] == '1' for row in image))
        right = search(y,len(image[0]),lambda y: all(row[y] == '0' for row in image))
        return (top-bottom)*(left-right)
