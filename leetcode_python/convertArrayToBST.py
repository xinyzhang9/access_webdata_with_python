# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.dfs(nums,0,len(nums)-1)
    
    def dfs(self,nums,start,end):
        if start > end:
            return None
        mid = start+(end-start)/2
        root = TreeNode(nums[mid])
        root.left = self.dfs(nums,start,mid-1)
        root.right = self.dfs(nums,mid+1,end)
        return root
