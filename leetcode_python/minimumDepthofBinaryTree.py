# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        now = []
        level = 0
        if root:
            now.append(root)
        while now:
            tmp = []
            level += 1
            for v in now:
                if v.left is None and v.right is None:
                    return level
                if v.left:
                    tmp.append(v.left)
                if v.right:
                    tmp.append(v.right)
            now = tmp
        return level
            