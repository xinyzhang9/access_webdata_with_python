# Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

# For example, given nums = [-2, 0, 1, 3], and target = 2.

# Return 2. Because there are two triplets which sums are less than 2:

# [-2, 0, 1]
# [-2, 0, 3]

class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = []
        if nums == []:
            return 0
        count = 0
        nums.sort()
        for i in range(0,len(nums)-1):
            left = i+1
            right = len(nums)-1
            while left < right:
                if nums[i]+nums[left]+nums[right] < target:
                    count += right-left
                    left += 1
                else:
                    right -= 1
        return count
        