# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

# For example:
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \      \
#         7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        # if root not exist, there is no solution
        if not root:
            return False
        # if the leaf node has value == current sum, we got the path
        if root.val == sum and root.left is None and root.right is None:
            return True
        # recursively find possible paths in left and right child
        return self.hasPathSum(root.left,sum-root.val) or self.hasPathSum(root.right,sum-root.val)