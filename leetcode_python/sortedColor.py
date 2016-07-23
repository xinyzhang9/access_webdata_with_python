# Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        red,white,blue = 0,0,len(nums)-1
        while white <= blue:
            if nums[white] == 0:
                nums[red],nums[white] = nums[white],nums[red]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[blue],nums[white] = nums[white],nums[blue]
                blue-=1 # don't write white+=1 !
                