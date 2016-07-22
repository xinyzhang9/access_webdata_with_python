# This is a follow up of Shortest Word Distance. The only difference is now word1 could be the same as word2.

# Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

# word1 and word2 may be the same and they represent two individual words in the list.

# For example,
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

# Given word1 = “makes”, word2 = “coding”, return 1.
# Given word1 = "makes", word2 = "makes", return 3.

class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        idx1,idx2 = -1,-1
        distance = sys.maxint
        for i in range(len(words)):
            word = words[i]
            if word == word1:
                idx1 = i
                if idx2 != -1:
                    if idx1 != idx2:
                        distance = min(distance,idx1-idx2)
                    
            if word == word2:
                idx2 = i
                if idx1 != -1:
                    if idx1 != idx2:
                        distance = min(distance,idx2-idx1)
        return distance