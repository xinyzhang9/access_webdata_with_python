# Given two arrays, write a function to compute their intersection.

# Example:
# Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

# Note:
# Each element in the result should appear as many times as it shows in both arrays.
# The result can be in any order.
# Follow up:
# What if the given array is already sorted? How would you optimize your algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is better?
# What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic = dict()
        res = []
        for v in nums1:
            if v not in dic:
                dic[v] = [1,0] # [counter in nums1, counter in mums2]
            else:
                dic[v][0] += 1
        for v in nums2:
            if v in dic:
                dic[v][1] += 1
        for k,v in dic.items():
            if v[0]*v[1] > 0: # v appear in both lists
                for i in range(min(v[0],v[1])):
                    res.append(k)
        return res
