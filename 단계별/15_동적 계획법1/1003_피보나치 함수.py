import sys
from collections import defaultdict

T = int(sys.stdin.readline())
for _ in range(T):
    dp = defaultdict(int)
    N = int(sys.stdin.readline())
    dp[0] = (1,0)
    dp[1] = (0,1)
    for i in range(2, N+1):
        dp[i] = (dp[i-1][0]+dp[i-2][0], dp[i-1][1]+dp[i-2][1])
    print(*dp[N])