# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start,end=1,n+1
        while start<end:
            mid = (end-start)/2+start
            if isBadVersion(mid):
                end=mid
            else:
                start=mid+1
        return start