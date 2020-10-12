#图的bfs，加visited记录访问过的节点，用一个map记录路径长短
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        distance = {beginWord: 1}
        visited = set([beginWord])
        from collections import deque
        queue = deque([beginWord])
        wordSet = set(wordList)
        while queue:
            item = queue.popleft()
            if item == endWord:
                return distance[item]
            
            for word in self.getNext(item):
                if word in wordSet and word not in visited:
                    queue.append(word)
                    visited.add(word)
                    distance[word] = distance[item] + 1
        return 0

    def getNext(self, item):
        words = []
        for i in range(len(item)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                newWord = item[:i] + c + item[i + 1:]
                words.append(newWord)
        return words

#doesn't need visited, already has the visited records--distance
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        distance = {beginWord: 1}
        from collections import deque
        queue = deque([beginWord])
        wordSet = set(wordList)
        while queue:
            item = queue.popleft()
            if item == endWord:
                return distance[item]
            for word in self.getNext(item):
                if word not in distance and word in wordSet:
                    queue.append(word)
                    distance[word] = distance[item] + 1
        return 0

    def getNext(self, item):
        words = []
        for i in range(len(item)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                new_item = item[:i] + c + item[i + 1:]
                words.append(new_item)
        return words
