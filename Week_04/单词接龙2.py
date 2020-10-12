# four functions
# 1: build indexes, for each word in wordList, index the key with corresponding words. key will be the word with one charactor replaced by "%"
# 2: getNext: return the neighbors which are the words in the indexes
# 3: bfs: start from endWord, record the shortest distance of each word in the wordList
# 4: dfs: start from startWord, dfs to the neighbors with 1 distance shorter than the word in the upper level
  
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        res = []
        if endWord not in wordList: return res
        wordSet = set(wordList)
        wordSet.add(beginWord)
        indexes = self.buildIndex(wordSet)
        distance = self.bfs(endWord, indexes) # records from end, the distance of each words in dict to end
        self.dfs(beginWord, endWord, [beginWord], distance, indexes, res)
        return res


    def buildIndex(self, wordSet):
        from collections import defaultdict
        indexes = defaultdict(list)
        for word in wordSet:
            for i in range(len(word)):
                key = word[:i] + "%" + word[i + 1:]
                if key in indexes:
                    indexes[key].append(word)
                else:
                    indexes[key] = [word]
        return indexes

    def getNext(self, item, indexes):
        words = []
        for i in range(len(item)):
            key = item[:i] + "%" + item[i + 1:]
            for value in indexes[key]:
                if value == item: continue
                words.append(value)
        return words

    def bfs(self, endWord, indexes):
        distance = {endWord: 0}
        from collections import deque
        queue = deque([endWord])
        while queue:
            item = queue.popleft()
            for word in self.getNext(item, indexes):
                if word not in distance:
                    queue.append(word)
                    distance[word] = distance[item] + 1
        return distance
    
    def dfs(self, currWord, endWord, path, distance, indexes, res):
        if currWord == endWord:
            res.append(path)
            return

        for word in self.getNext(currWord, indexes):
            if distance[word] == distance[currWord] - 1:
                self.dfs(word, endWord, path + [word], distance, indexes, res)
         

