#p[:i - 1], s[:j - 1] 
# two scenarios
# 1. p[i] == s[j], dp[i][j] = dp[i - 1][j - 1]
# 2. p[i] != s[j], if p[i] == "?", match, dp[i][j] = dp[i - 1][j - 1]
                   # if p[i] == "*", match p[j] or "", dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                   
#.       ""  a   a    b     
# "" true false false
# c false  false false
# *  true   

#     " " c  *
# " " true false 
#注意事项
#初始化矩阵的大小，比字符串大小+1
#遍历字符串，矩阵下标比字符串下标大1
#对于*初始化，True or false 取决于前一个元素的True or false
#对于*, 可以选择match, then dp[i][j] = dp[i][j - 1], i 代表pattern, * keep in the pattern
也可以选择不match, 空字符，then dp[i][j] = dp[i - 1][j]

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (1 + len(s)) for _ in range(len(p) +1)]
        dp[0][0] = True
        for i in range(1, len(p) + 1):
            if p[i - 1] == "*":
                dp[i][0] = dp[i - 1][0]
        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                if p[i - 1] == s[j - 1] or p[i - 1] == "?":
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[i - 1] == "*":
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
        return dp[len(p)][len(s)]
