# Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

# For example,
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

# Given word1 = “coding”, word2 = “practice”, return 3.
# Given word1 = "makes", word2 = "coding", return 1.

# Note:
# You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

# my solution, a little bit slow
class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        list1 = []
        list2 = []
        for i in range(len(words)):
            word = words[i]
            if word == word1:
                list1.append(i)
            if word == word2:
                list2.append(i)
        min_v = abs(list1[0]-list2[0])
        index1 = 0
        index2 = 0
        while index1 < len(list1) and index2 < len(list2):
            if list1[index1] < list2[index2]:
                min_v = min(min_v,abs(list1[index1]-list2[index2]))
                index1+=1
            else:
                min_v = min(min_v,abs(list1[index1]-list2[index2]))
                index2+=1
        return min_v
        

# better solution
class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        idx1 = -1
        idx2 = -1
        distance = sys.maxint
        for i in range(len(words)):
            if words[i] == word1:
                idx1 = i
                if idx2 != -1:
                    distance = min(distance,idx1-idx2)
            if words[i] == word2:
                idx2 = i
                if idx1 != -1:
                    distance = min(distance,idx2-idx1)
        return distance
        