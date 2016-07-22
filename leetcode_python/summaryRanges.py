# Given a sorted integer array without duplicates, return the summary of its ranges.

# For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        if nums == []:
            return res;
        if len(nums) == 1:
            return [str(nums[0])]
            
        start = nums[0]
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1] == 1:
                if i== len(nums)-1:
                    seg = str(start)+'->'+str(nums[i])
                    res.append(seg)
            else:
                if start == nums[i-1]:
                    seg = str(start)
                else:
                    seg = str(start)+'->'+str(nums[i-1])
                res.append(seg)
                if i== len(nums)-1:
                    seg = str(nums[i])
                    res.append(seg)
                else:
                    start = nums[i]
        return res