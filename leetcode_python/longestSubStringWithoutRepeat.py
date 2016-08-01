class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return len(s)
        start,end = 0,1
        res = 1
        dic = dict()
        dic[s[start]] = start
        while end < len(s):
            while s[end] not in dic:
                dic[s[end]] = end
                print dic
                res = max(res,len(dic))
                end += 1
                if end >= len(s):
                    return res
            print dic
            dic = {k: v for k, v in dic.iteritems() if v > dic[s[end]]}
            print dic
            # start,end = end,start+1
            # dic[s[start]] = start
        return res

s = Solution()
test = "ohvhjdml"
print s.lengthOfLongestSubstring(test)