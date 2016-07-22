# Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

#     For example, given array S = {-1 2 1 -4}, and target = 1.

#     The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = sys.maxint
        for i in range(len(nums)-1):
            v = nums[i]
            left,right = i+1,len(nums)-1
            while left < right:
                s = v+nums[left]+nums[right]
                if s == target:
                    return target
                elif s < target:
                    if target - s < abs(target - res):
                        res = s
                    left += 1
                else:
                    if s-target < abs(res-target):
                        res = s
                    right -= 1
        return res
            