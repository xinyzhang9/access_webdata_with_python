# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        pre, cur, first, second = None, root, None, None
        while cur:
            if not cur.left:
                if pre != None and pre.val > cur.val:
                    if not first: first = pre
                    second = cur
                pre, cur = cur, cur.right
            else:
                p = cur.left
                while p.right and p.right != cur: p = p.right
                if not p.right:
                    p.right = cur
                    cur = cur.left
                else:
                    p.right = None
                    if pre != None and pre.val > cur.val:
                        if not first: first = pre
                        second = cur
                    pre, cur = cur, cur.right
        first.val, second.val = second.val, first.val
        