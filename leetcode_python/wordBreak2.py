# Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

# Return all such possible sentences.

# For example, given
# s = "catsanddog",
# dict = ["cat", "cats", "and", "sand", "dog"].

# A solution is ["cats and dog", "cat sand dog"].

class Solution(object):
    memory = dict()
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        if s in self.memory:
            return self.memory[s]
        res = []
        if s in wordDict:
            res.append(s)
        for i in range(1,len(s)):
            word = s[i:]
            if word in wordDict:
                rem = s[0:i]
                prev = self.combine(word,self.wordBreak(rem,wordDict))
                res+=prev
        self.memory[s] = res
        return res
        
    
    def combine(self,word,lists):
        for i in range(len(lists)):
            lists[i] += " "+word
        return lists