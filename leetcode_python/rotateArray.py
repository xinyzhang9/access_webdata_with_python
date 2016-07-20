class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        self.reverse(nums,0,len(nums)-k-1)
        self.reverse(nums,len(nums)-k,len(nums)-1)
        self.reverse(nums,0,len(nums)-1)
        
    def reverse(self, nums, i, j):
        while i < j:
            nums[i],nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
            
                
s = Solution()
nums = [1,2,3,4,5,6,7]
s.rotate(nums,3)
print nums