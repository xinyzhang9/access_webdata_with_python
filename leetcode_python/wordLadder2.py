# Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

# Only one letter can be changed at a time
# Each intermediate word must exist in the word list
# For example,

# Given:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# Return
#   [
#     ["hit","hot","dot","dog","cog"],
#     ["hit","hot","lot","log","cog"]
#   ]
# Note:
# All words have the same length.
# All words contain only lowercase alphabetic characters.

class Solution(object):
    def _build(self,parent,path,paths):
        if not parent[path[-1]]:
            paths.append(path[:])
            return
        for nextWord in parent[path[-1]]:
            path.append(nextWord)
            self._build(parent,path,paths)
            path.pop()
            
    def buildLadders(self,aWord,bWord,beginWord,parent,ans):
        paths = [[],[]]
        path = [aWord]
        self._build(parent,path,paths[0])
        path = [bWord]
        self._build(parent,path,paths[1])
        if paths[0][0][-1] != beginWord:
            paths.reverse()
        for path in paths[0]:
            path.reverse()
        for aPath in paths[0]:
            for bPath in paths[1]:
                ans.append(aPath + bPath)
                
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        fronts = [{beginWord},{endWord}]
        parent = {beginWord:None,endWord:None}
        wordlist.discard(beginWord)
        wordlist.discard(endWord)
        ans = []
        while fronts[0] and fronts[1] and not ans:
            if len(fronts[0]) > len(fronts[1]):
                fronts.reverse()
            newLevel = set()
            for word in fronts[0]:
                for i in xrange(len(beginWord)):
                    for char in string.lowercase:
                        newWord = word[:i] + char + word[i+1:]
                        if newWord in fronts[1]:
                            self.buildLadders(word,newWord,beginWord,parent,ans)
                        if newWord in newLevel:
                            parent[newWord].append(word)
                        if newWord in wordlist:
                            newLevel.add(newWord)
                            wordlist.discard(newWord)
                            parent[newWord] = [word]
            fronts[0] = newLevel
        return ans