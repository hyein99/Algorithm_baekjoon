# i번째 집을 각각의 색으로 칠할 때 1~i번째 집을 모두 칠하는 최소비용으로 부분 문제 정의

import sys
from collections import defaultdict

def get_cost(N):
    dp = defaultdict(int)
    dp[0] = clist[0]
    # dp[i][j]: i번째 집에 j번째 색을 선택했을 때 비용의 최소값
    for i in range(1, N):
        dp[i] = [min(dp[i-1][1], dp[i-1][2]) + clist[i][0],
                 min(dp[i-1][0], dp[i-1][2]) + clist[i][1],
                 min(dp[i-1][0], dp[i-1][1]) + clist[i][2]]
    return min(dp[N-1])


# 입력
N = int(sys.stdin.readline())
clist = []
for _ in range(N):
    clist.append(list(map(int, sys.stdin.readline().split())))
print(get_cost(N))
