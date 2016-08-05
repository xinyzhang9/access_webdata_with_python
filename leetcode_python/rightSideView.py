# Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# For example:
# Given the following binary tree,
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---
# You should return [1, 3, 4].

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if root is None:
            return res
        self.dfs(root,res,0)
        return res
        
    def dfs(self,root,res,depth):
        if root is None:
            return
        # each level, only add one value
        if depth == len(res):
            res.append(root.val)
        self.dfs(root.right,res,depth+1)
        self.dfs(root.left,res,depth+1)