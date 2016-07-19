class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return False
        dic = dict()
        for i in range(len(nums)):
            v = nums[i]
            if v in dic:
                return True
            dic[v] = i
        return False