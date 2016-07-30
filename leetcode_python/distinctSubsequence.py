# Given a string S and a string T, count the number of distinct subsequences of T in S.

# A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

# Here is an example:
# S = "rabbbit", T = "rabbit"

# Return 3.

# https://discuss.leetcode.com/topic/9488/easy-to-understand-dp-in-java
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        dp = [[0]*(len(s)+1) for x in range(len(t)+1)]
        dp[0] = [1]*(len(s)+1)
        for i in range(len(t)):
            for j in range(len(s)):
                if s[j] != t[i]:
                    dp[i+1][j+1] = dp[i+1][j]
                else:
                    dp[i+1][j+1] = dp[i+1][j] + dp[i][j]
        return dp[-1][-1]
