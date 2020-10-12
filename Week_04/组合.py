#从n里面选k个，第一个数有n个选择，第二个数有n-1个选择，为了避免重复，结果的数组升序排列

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if not k or not n: return []
        self.res = []
        self.dfs(n, 0, k, [])
        return self.res

    def dfs(self, n, level, k, combine):
        if level == k:
            if len(combine) == k:
                self.res.append(combine)
            return

        for i in range(1, n + 1):
            if i in combine: continue
            if combine and i < combine[-1]: continue
            self.dfs(n, level + 1, k, combine + [i])

#在选择的过程中选择有重复，记录上一次访问的数begin

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if not k or not n: return []
        self.res = []
        self.dfs(n, 1, k, [])
        return self.res

    def dfs(self, n, begin, k, combine):
        if len(combine) == k:
            self.res.append(combine)
            return

        for i in range(begin, n + 1):
            self.dfs(n, i + 1, k, combine + [i])

#在选择循环上限的时候剪纸，循环开始的上限是 n + 1 - (k - len(combine)) + 1
#假如 n = 7, len(combine) = 1, k = 4, 循环开始的最大值是 7 + 1 - （4 - 1）= 5， 可以选【5， 6， 7】
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if not k or not n: return []
        self.res = []
        self.dfs(n, 1, k, [])
        return self.res

    def dfs(self, n, begin, k, combine):
        if len(combine) == k:
            self.res.append(combine)
            return

        for i in range(begin, n - (k - len(combine)) + 1 + 1):
            self.dfs(n, i + 1, k, combine + [i])


