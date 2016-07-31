# A message containing letters from A-Z is being encoded to numbers using the following mapping:

# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given an encoded message containing digits, determine the total number of ways to decode it.

# For example,
# Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

# The number of ways decoding "12" is 2.

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        n = len(s)
        
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1
        print dp
        for i in range(2,n+1):
            first = int(s[i-1:i])
            second = int(s[i-2:i])
            if 1 <= first and first <= 9:
                dp[i] += dp[i-1]
            if 10<= second and second <= 26:
                dp[i] += dp[i-2]
            print dp
                    
        return dp[n]

s = Solution()
t = '10'
s.numDecodings(t)