# Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum ≥ s. If there isn't one, return 0 instead.

# For example, given the array [2,3,1,2,4,3] and s = 7,
# the subarray [4,3] has the minimal length under the problem constraint.

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        start,sums,res = 0,0,len(nums)+1
        for i in range(len(nums)):
            sums += nums[i]
            while sums >=s:
                res = min(res,i-start+1)
                sums -= nums[start]
                start += 1
        return res if res != len(nums)+1 else 0
        