# Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

# Solve it without division and in O(n).

# For example, given [1,2,3,4], return [24,12,8,6].

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1]*len(nums)
        for i in range(1,len(nums)):
            res[i] = res[i-1]*nums[i-1]
        right = 1
        for i in reversed(range(len(nums))):
            res[i] *= right
            right *= nums[i]
        return res