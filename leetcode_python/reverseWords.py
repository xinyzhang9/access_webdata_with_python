class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        print s.split(' ')[::-1]
        return ' '.join(i for i in s.split(' ')[::-1] if i != '')

s = Solution()
test = 'a nice   word '
print s.reverseWords(test)