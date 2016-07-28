# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

# For "(()", the longest valid parentheses substring is "()", which has length = 2.

# Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.


''' 
My solution uses DP. The main idea is as follows: I construct a array longest[], for any longest[i], it stores the longest length of valid parentheses which is end at i.

And the DP idea is :

If s[i] is '(', set longest[i] to 0,because any string end with '(' cannot be a valid one.

Else if s[i] is ')'

     If s[i-1] is '(', longest[i] = longest[i-2] + 2

     Else if s[i-1] is ')' and s[i-longest[i-1]-1] == '(', longest[i] = longest[i-1] + 2 + longest[i-longest[i-1]-2]

For example, input "()(())", at i = 5, longest array is [0,2,0,0,2,0], longest[5] = longest[4] + 2 + longest[1] = 6.
'''

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return 0
        n = len(s)
        dp = [0]*n
        for i in range(1,n):
            if s[i] == ')':
                if s[i-1] == '(':
                    if i-2 >=0:
                        dp[i] = dp[i-2]+2
                    else:
                        dp[i] = 2
                else:
                    if i-dp[i-1]-1 >=0 and s[i-dp[i-1]-1] == '(':
                        if i-dp[i-1]-2 >=0:
                            dp[i] = dp[i-1]+2+dp[i-dp[i-1]-2]
                        else:
                            dp[i] = dp[i-1]+2

        return max(dp)
