# Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

# Example:
# For num = 5 you should return [0,1,1,2,1,2].

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        dp = [0]*(num+1)
        for i in range(num+1):
            dp[i] = dp[i>>1] + (i & 1)
        return dp