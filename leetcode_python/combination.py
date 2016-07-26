# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

# For example,
# If n = 4 and k = 2, a solution is:

# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        if k < 1 or k > n:
            return res
        self.backtrack(n+1,k,[],res,1)
        return res
    
    def backtrack(self,max_v,k,tmpList,res,start):
        
        if k == len(tmpList):
            res.append(list(tmpList))
        else:
            for i in range(start,max_v):
                # stop earlier if there is not enough values to fill in the k-length array
                if max_v-i+1 + len(tmpList) < k:
                    return
                tmpList.append(i)
                self.backtrack(max_v,k,tmpList,res,i+1)
                tmpList.pop()
                