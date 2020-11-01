#自顶向下，recursion + memorization
class Solution:
    import functools
    @functools.lru_cache(None)
    def minDistance(self, word1: str, word2: str) -> int:
        if not len(word1) or not len(word2):
            return len(word1) + len(word2)
        if word1[-1] == word2[-1]:
            return self.minDistance(word1[:-1], word2[:-1])
        else:
            insert = self.minDistance(word1, word2[:-1])
            delete = self.minDistance(word1[:-1], word2)
            replace = self.minDistance(word1[:-1], word2[:-1])
            return min(insert, delete, replace) + 1

#自底向上，op initialization = recursion terminator

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        if not word1 or not word2: return m + n 
        op = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            op[i][0] = i

        for j in range(m + 1):
            op[0][j] = j

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    op[i][j] = op[i - 1][j - 1]
                else:
                    op[i][j] = min(op[i - 1][j], op[i][j - 1], op[i - 1][j - 1]) + 1
        return op[i][j]

