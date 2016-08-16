# Given a sorted array of integers nums and integer values a, b and c. Apply a function of the form f(x) = ax2 + bx + c to each element x in the array.

# The returned array must be in sorted order.

# Expected time complexity: O(n)

# Example:
# nums = [-4, -2, 2, 4], a = 1, b = 3, c = 5,

# Result: [3, 9, 15, 33]

# nums = [-4, -2, 2, 4], a = -1, b = 3, c = 5

# Result: [-23, -5, 1, 7]

class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        def calc(nums,i):
            return a*nums[i]*nums[i] + b*nums[i]+c
        res = [0]*len(nums)
        left,right = 0,len(nums)-1
        index = len(nums)-1 if a>0 else 0
        if a == 0:
            if b >0:
                return map(lambda x: b*x+c,nums)
            else:
                return map(lambda x: b*x+c,reversed(nums))
                
        while left <=right:
            if a > 0:
                if calc(nums,left) >= calc(nums,right):
                    res[index] = calc(nums,left)
                    left += 1
                else:
                    res[index] = calc(nums,right)
                    right -= 1
                index -= 1
            else:
                if calc(nums,left) <= calc(nums,right):
                    res[index] = calc(nums,left)
                    left += 1
                else:
                    res[index] = calc(nums,right)
                    right -= 1
                index += 1
                
        return res