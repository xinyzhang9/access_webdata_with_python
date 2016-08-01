# Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1...n.

# For example,
# Given n = 3, your program should return all 5 unique BST's shown below.

#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n==0:
            return []
        return self.dfs(1,n)
    
    def dfs(self,start,end):
        if start > end:
            return [None]
        res = []
        for v in range(start,end+1):
            left = self.dfs(start,v-1)
            right = self.dfs(v+1,end)
            for i in left:
                for j in right:
                    root = TreeNode(v)
                    root.left = i
                    root.right = j
                    res.append(root)
        return res