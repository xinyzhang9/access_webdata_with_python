class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = dict();
        for i in range(len(nums)):
            x = nums[i]
            if target-x in dic:
                return (dic[target-x],i)
            dic[x] = i