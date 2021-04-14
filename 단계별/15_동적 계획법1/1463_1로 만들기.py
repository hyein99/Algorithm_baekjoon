# 메모이제이션으로 N을 1로 바꾸기 위해 주어진 연산을 몇 번 사용하는지 계산하는 문제

import sys
from collections import defaultdict

# 메모이제이션: Recursion Error
# dp = defaultdict(int)
# def make_one(N):
#     # 초기값 설정
#     if N==1:
#         return 0
#     if N==2 or N==3:
#         return 1
#     if dp[N]:
#         return dp[N]
#
#     if N%6==0:
#         dp[N] = 1 + min(make_one(N//3), make_one(N//2), make_one(N-1))
#         return dp[N]
#     elif N%3==0:
#         dp[N] = 1 + min(make_one(N//3), make_one(N-1))
#         return dp[N]
#     elif N%2==0:
#         dp[N] = 1 + min(make_one(N//2), make_one(N-1))
#         return dp[N]
#     else:
#         dp[N] = 1 + make_one(N-1)
#         return dp[N]

# 타뷸레이션
dp = defaultdict(int)
def make_one(N):
    # 초기값 설정
    if N==1:
        return 0
    if N==2 or N==3:
        return 1
    dp[1], dp[2], dp[3] = 0, 1, 1

    for i in range(4, N+1):
        if i%6==0:
            dp[i] = 1 + min(dp[i//3], dp[i//2], dp[i-1])
        elif i%3==0:
            dp[i] = 1 + min(dp[i//3], dp[i-1])
        elif i%2==0:
            dp[i] = 1 + min(dp[i//2], dp[i-1])
        else:
            dp[i] = 1 + dp[i-1]
    return dp[N]


N = int(sys.stdin.readline())
print(make_one(N))