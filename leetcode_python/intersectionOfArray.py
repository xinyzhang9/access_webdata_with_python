# Given two arrays, write a function to compute their intersection.

# Example:
# Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic = dict()
        res = []
        for v in nums1:
            if v not in dic:
                dic[v] = False
        for v in nums2:
            if v in dic:
                dic[v] = True
        for k,v in dic.items():
            if v:
                res.append(k)
        return res