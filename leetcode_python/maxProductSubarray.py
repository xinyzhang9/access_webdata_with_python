# Find the contiguous subarray within an array (containing at least one number) which has the largest product.

# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        f = []
        g = []
        f.append(nums[0])
        g.append(nums[0])
        for i in range(1,len(nums)):
            f.append(max(f[i-1]*nums[i],g[i-1]*nums[i],nums[i]))
            g.append(min(f[i-1]*nums[i],g[i-1]*nums[i],nums[i]))
        return max(f)