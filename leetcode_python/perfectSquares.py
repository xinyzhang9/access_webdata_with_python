# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

# For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        toCheck = {n}
        cnt = 0
        while toCheck:
            cnt += 1
            lst = []
            nextCheck = set()
            i = 1
            while i*i <= n:
                lst.append(i*i)
                i += 1
            for c in toCheck:
                for j in lst:
                    if c<j:
                        break
                    if c==j:
                        return cnt
                    nextCheck.add(c-j)
            toCheck = nextCheck
        
        return cnt
        