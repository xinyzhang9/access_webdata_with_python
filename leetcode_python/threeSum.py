class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        length = len(nums)
        for i in range(0,length-2):
            if i and nums[i] == nums[i-1]:
                continue
            target = nums[i]
            left,right = i+1,length-1
            while left < right:
                if nums[left]+nums[right]+target == 0:
                    res.append([nums[i],nums[left],nums[right]])
                    right-=1
                    left+=1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif nums[left]+nums[right]+target < 0:
                    left+=1
                else:
                    right-=1
        return res
        