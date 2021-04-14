# 1, 1, 1, 2, 2, 3, 4, 5, 7, 9...

import sys

def P(N):
    dp = [0]*101
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    for i in range(4, N+1):
        dp[i] = dp[i-2]+dp[i-3]
    return dp[N]

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    print(P(N))
