# Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

# Note:
# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n2).
# There is only one duplicate number in the array, but it could be repeated more than once.

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        low,high = 0,len(nums)-1
        while low < high:
            cnt = 0
            mid = low+(high-low)/2
            print 'low','high','mid',low,high,mid
            for i in range(len(nums)):
                if nums[i] <= mid:
                    cnt += 1
            print 'cnt',cnt
            if cnt > mid:
                high = mid
            else:
                low = mid+1
            
        
        print low
        return low

s = Solution()
s.findDuplicate([1,3,5,2,4,3])
