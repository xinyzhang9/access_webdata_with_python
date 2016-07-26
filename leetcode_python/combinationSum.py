# Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

# The same repeated number may be chosen from C unlimited number of times.

# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# For example, given candidate set [2, 3, 6, 7] and target 7, 
# A solution set is: 
# [
#   [7],
#   [2, 2, 3]
# ]

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        # I think candidates should be sorted first
        self.backtrack(candidates,target,[],res,0)
        return res
        
    def backtrack(self,candidates,target,tmpList,res,start):
        if target < 0:
            return
        if target == 0:
            res.append(list(tmpList)) # copy list, don't use reference
        else:
            for i in range(start,len(candidates)):
                tmpList.append(candidates[i])
                self.backtrack(candidates,target-candidates[i],tmpList,res,i)
                tmpList.pop()
            