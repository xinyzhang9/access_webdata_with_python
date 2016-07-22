# A peak element is an element that is greater than its neighbors.

# Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

# The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

# You may imagine that num[-1] = num[n] = -∞.

# For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1 :
            return 0
        if len(nums) == 2 :
            return [0,1][nums[0] < nums[1]]

        left,right = 0,len(nums)-1
        while left+1 < right:
            mid = (right-left)/2 + left
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid] < nums[mid-1]:
                right = mid
            elif nums[mid] < nums[mid+1]:
                left = mid
                
        if nums[mid] < nums[right]:
            return right
        if nums[mid] < nums[left]:
            return left
        return mid