# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        return self.build(head,None)
    
    def build(self,start,end):
        if start == end:
            return None
        slow,fast = start,start
        while fast != end and fast.next != end:
            slow = slow.next
            fast = fast.next.next
        root = TreeNode(slow.val)
        root.left = self.build(start,slow)
        root.right = self.build(slow.next,end)
        return root
