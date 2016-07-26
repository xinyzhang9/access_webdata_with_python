# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

# For example,
# Given nums = [0, 1, 3] return 2.

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if not nums:
        #     return 0
        # return len(nums)*(len(nums)+1)/2 - sum(nums)
        res = len(nums)
        for i in range(len(nums)):
            res ^= i ^ nums[i]
        return res

# [0,1,2,3] -- index
# [0,1,2,4] -- array

# res = 4 ^ 0 ^ 0 ^ 1 ^ 1 ^ 2 ^ 2 ^ 3 ^4 = 3
# since a ^ b ^ b = a