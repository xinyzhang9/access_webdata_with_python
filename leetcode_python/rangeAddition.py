class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        res = [0]*(length+1)
        # for update in updates:
        #     start,end,inc = update
        #     res[:end+1] = map(lambda x:x+inc,res[:end+1])
        #     if start > 0:
        #         res[:start] = map(lambda x:x-inc,res[:start])
        # return res
        
        for update in updates:
            start,end,inc = update
            res[start] += inc
            res[end+1] -= inc
        for i in range(1,len(res)):
            res[i] += res[i-1]
        res.pop()
        return res
            


s = Solution()
updates = [[1,3,2],[2,4,3],[0,2,-2]]
print s.getModifiedArray(5,updates)