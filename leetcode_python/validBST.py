# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.dfs(root,-sys.maxint-1, sys.maxint)
        
    def dfs(self,root,min_v,max_v):
        if not root:
            return True
        if root.val >=max_v or root.val <= min_v:
            return False
        return self.dfs(root.left,min_v,root.val) and self.dfs(root.right,root.val,max_v)