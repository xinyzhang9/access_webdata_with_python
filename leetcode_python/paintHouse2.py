import sys
class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0
        n,k = len(costs),len(costs[0])
        preMin,preSec,preIdx = 0,0,-1
        for i in range(n):
            curMin,curSec,curIdx = sys.maxint,sys.maxint,-1
            for j in range(k):
                costs[i][j] += preSec if preIdx == j else preMin
                if costs[i][j] < curMin:
                    curSec = curMin
                    curMin = costs[i][j]
                    curIdx = j
                elif costs[i][j] < curSec:
                    curSec = costs[i][j]
            preMin,preSec,preIdx = curMin,curSec,curIdx
            print preMin,preSec,preIdx
        return preMin

s = Solution()
costs = [[1,5,3],[2,9,4]]
s.minCostII(costs)