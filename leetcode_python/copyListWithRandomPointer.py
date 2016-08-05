# A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

# Return a deep copy of the list.

# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        # insert nodes
        cur = head
        while cur:
            next = cur.next
            copy = RandomListNode(cur.label)
            copy.next = cur.next
            cur.next = copy
            cur = next
        # copy random pointer
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        # decouple two links
        cur = head
        if head:
            dup = head.next
        else:
            dup = None
        while cur:
            tmp = cur.next
            cur.next = tmp.next
            if tmp.next:
                tmp.next = tmp.next.next
            cur = cur.next
        return dup
            
        