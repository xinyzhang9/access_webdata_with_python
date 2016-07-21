class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        nums.sort()
        for num in nums:
            res +=[k + [num] for k in res if k+[num] not in res]
        return res
        
                