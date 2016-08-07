# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

# An example is the root-to-leaf path 1->2->3 which represents the number 123.

# Find the total sum of all root-to-leaf numbers.

# For example,

#     1
#    / \
#   2   3
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.

# Return the sum = 12 + 13 = 25.

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        sum = 0
        res = []
        self.findAllPaths(root,[],res)
        for path in res:
            sum += self.getSum(path)
        return sum
    
    def findAllPaths(self,root,path,res):
        if root is None:
            return
        path.append(root.val)
        if root.left is None and root.right is None:
            res.append(list(path))
        self.findAllPaths(root.left,path,res)
        self.findAllPaths(root.right,path,res)
        path.pop()
    
    def getSum(self,path):
        sum = 0
        i = 1
        for v in reversed(path):
            sum += v*i
            i*=10
        return sum