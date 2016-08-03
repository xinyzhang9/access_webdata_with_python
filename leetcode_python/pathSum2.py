# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

# For example:
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# return
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def dfs(root,res,path,sum):
            # the path is not valid if current root is None
            if not root:
                return
            # add current root value to path
            path.append(root.val)
            # valid path, append to final solution
            if root.val == sum and root.left is None and root.right is None:
                res.append(list(path))
            # recursively find possible solutions
            dfs(root.left,res,path,sum-root.val)
            dfs(root.right,res,path,sum-root.val)
            # before return to previous level, reset the path to previous status
            path.pop()
            
        if not root:
            return []
        res = []
        path = [] # path records node series up to now, which is possible to make up a valid solution
        dfs(root,res,path,sum)
        return res
        