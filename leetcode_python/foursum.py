# Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

# Note: The solution set must not contain duplicate quadruplets.

# For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        if len(nums) < 4:
            return res
        nums.sort()
        for i in range(len(nums)-3):
            if i and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,len(nums)-2):
                if j!=i+1 and nums[j] == nums[j-1]:
                    continue
                left,right = j+1,len(nums)-1
                sums = target-nums[i]-nums[j]
                while left < right:
                    if nums[left]+nums[right] == sums:
                        res.append(list([nums[i],nums[j],nums[left],nums[right]]))
                        left += 1
                        right -= 1
                        while left  < right and nums[left] == nums[left-1]:
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
                    elif nums[left]+nums[right] < sums:
                        left += 1
                    else:
                        right -= 1
        return res
                        