# Note: This is an extension of House Robber.

# After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the previous street.

# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        def robHelper(nums):
            if not nums:
                return 0
            if len(nums) == 1:
                return nums[0]
            dp = [0]*len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0],nums[1])
            for i in range(2,len(nums)):
                dp[i] = max(dp[i-1],dp[i-2]+nums[i])
            return dp[-1]
        return max(robHelper(nums[1:]),robHelper(nums[:-1]))
        