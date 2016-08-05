# Given a binary tree, return all root-to-leaf paths.

# For example, given the following binary tree:

#    1
#  /   \
# 2     3
#  \
#   5
# All root-to-leaf paths are:

# ["1->2->5", "1->3"]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     # @param {TreeNode} root
#     # @return {string[]}
#     def binaryTreePaths(self, root):
#         res = []
#         if not root:
#             return res
#         self.dfs(root,res,[])
#         for x in range(len(res)):
#             res[x] = "->".join(str(i) for i in res[x])
#         return res
#     def dfs(self,root,res,path):
#         if not root:
#             return
#         path.append(root.val)
#         if root.left is None and root.right is None:
#             res.append(list(path))
#         self.dfs(root.left,res,path)
#         self.dfs(root.right,res,path)
#         path.pop()

# improved version
class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        res = []
        if not root:
            return res
        self.dfs(root,"",res)
        return res
        
    def dfs(self,root,path,res):
        if root.left is None and root.right is None:
            res.append(path+str(root.val))
        if root.left:
            self.dfs(root.left,path+str(root.val)+'->',res)
        if root.right:
            self.dfs(root.right,path+str(root.val)+'->',res)