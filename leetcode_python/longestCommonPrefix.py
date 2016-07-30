class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        res = strs[0]
        for s in strs:
            # if res has shrinked to empty or encounter an empty string, return result immediately
            if s == "" or res == "":
                return ""
            # if res == s, skip to next string
            if s == res:
                continue
            # compare res and other string from from index 0
            startIndex = 0
            # find the break point where the common prefix may shrink
            while startIndex < len(s) and startIndex < len(res) and s[startIndex] == res[startIndex]:
                startIndex += 1
            # update the res
            res = res[0:startIndex]
        return res
            