import sys
from collections import defaultdict
input = sys.stdin.readline

# 입력
dp = defaultdict(int)
dp[0] = (1, 0)
dp[1] = (0, 1)
T = int(input())
max_N = 1
for _ in range(T):
    N = int(input())
    for i in range(max_N+1, N+1):
        dp[i] = (dp[i-1][0]+dp[i-2][0], dp[i-1][1]+dp[i-2][1])
    max_N = max(max_N, N)
    print(*dp[N])