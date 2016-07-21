# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

# For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
# the contiguous subarray [4,−1,2,1] has the largest sum = 6.
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        f = []
        f.append(nums[0])
        for i in range(1,len(nums)):
            f.append(max(f[i-1]+nums[i],nums[i]))
        max_v = f[0]
        for i in range(len(f)):
            if f[i] > max_v:
                max_v = f[i]
        return max_v