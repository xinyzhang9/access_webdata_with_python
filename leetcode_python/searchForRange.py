# Given a sorted array of integers, find the starting and ending position of a given target value.

# Your algorithm's runtime complexity must be in the order of O(log n).

# If the target is not found in the array, return [-1, -1].

# For example,
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return [3, 4].

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = [-1,-1]
        if not nums:
            return res
        x,y = -1,-1
        left,right = 0,len(nums)-1
        while left < right:
            mid = (right-left)/2 + left
            if nums[mid] < target:
                left = mid+1
            else:
                right = mid
        if nums[left] != target:
            return res
        else:
            res[0] = left
        
        right = len(nums)-1
        
        while left < right:
            mid = (right-left)/2 + left + 1 # make mid biased to the right
            if nums[mid] > target:
                right = mid-1
            else:
                left = mid
        res[1] = right
        return res