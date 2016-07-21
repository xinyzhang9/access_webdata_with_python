# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # ans = []
        # if numRows < 1:
        #     return ans
        # if numRows == 1:
        #     ans.append([1])
        #     return ans
        # if numRows == 2:
        #     ans.append([1])
        #     ans.append([1,1])
        #     return ans
            
        # ans.append([1])
        # ans.append([1,1])
        # last = [1,1]
        # for i in range(3,numRows+1,1):
        #     list = []
        #     for j in range(0,len(last)-1,1):
        #         list.append(last[j]+last[j+1])
        #     list = [1]+list+[1]
        #     last = list
        #     ans.append(list)
        # return ans
        res = [[1]]
        for i in range(1,numRows):
            res += [map(lambda x,y:x+y,res[-1]+[0],[0]+res[-1])]
        return res[:numRows]
                