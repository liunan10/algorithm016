class Solution:
    def checkRecord(self, n: int) -> int:
        # mod 1000000007
        #consider L and P, 
        #subproblem 1. n - 1 "ending with p"
        #subproblem 2. n - 2 "ending with pl"
        #subproblem 3. n - 3 "ending with pll"
        #op[n] = op[n - 1] + op[n - 2] + op[n - 3]
        #contains only one a
        #res = op[n - i] * op[i - 1]

        #only consider L and P
        MOD = 1000000007
        op = [1] * (n + 1)
        op[0] = 1
        if n >= 1: op[1] = 2
        if n >= 2: op[2] = 4
        for i in range(3, n + 1):
            op[i] = op[i - 1] + op[i - 2] + op[i - 3]
            op[i] %= MOD

        #consider A
        res = 0
        for i in range(1, n + 1):
            res += (op[i - 1] * op[n - i]) % MOD
        return (op[n] + res) %MOD
