# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         if len(s) < 2:
#             return len(s)
#         start,end = 0,1
#         res = 1
#         dic = dict()
#         dic[s[start]] = start
#         while end < len(s):
#             while s[end] not in dic:
#                 dic[s[end]] = end
#                 print dic
#                 res = max(res,len(dic))
#                 end += 1
#                 if end >= len(s):
#                     return res
#             print dic
#             dic = {k: v for k, v in dic.iteritems() if v > dic[s[end]]}
#             print dic
#         return res

# improved version
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return len(s)
        #make an ascii dictionary with value -1
        dic = dict( (chr(v), -1) for v in range(256) )
        start,res = 0,0
        for i in range(len(s)):
            if dic[s[i]] >= start:
                res = max(res,i-start)
                start = dic[s[i]] + 1
            dic[s[i]] = i
        return max(res,len(s)-start)

s = Solution()
test = "ohvhjdml"
print s.lengthOfLongestSubstring(test)