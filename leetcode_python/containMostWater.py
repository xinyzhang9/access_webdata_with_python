class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        res = 0
        left,right = 0,len(height)-1
        while left < right:
            res = max(res,min(height[left],height[right])*(right-left))
            if height[left] < height[right]: # move the less higher one
                k = left+1
                while k < right and height[k] <= height[left]: # until find some k, height[k] > height[left]
                    k += 1
                left = k
            else:
                k = right-1
                while k > left and height[k] <= height[right]:
                    k-= 1
                right = k
        return res