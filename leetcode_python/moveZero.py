# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

# Note:
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        idx0 = 0 # first possible position of 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[idx0],nums[i] = nums[i],nums[idx0]
                idx0 += 1 #after swap, the first possible position of 0 must + 1
        
        
        