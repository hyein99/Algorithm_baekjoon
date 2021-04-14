import sys
from collections import defaultdict

# dp[i] = max(dp[i-3]+stairs[i-1]+stairs[i], dp[i-2]+stairs[i])

# 타뷸레이션(상향식)
dp = defaultdict()
def get_stairs_sum(n):
    if n==1:   # 1, 2는 직접 설정
        return stairs[0]
    elif n==2:
        return stairs[0]+stairs[1]
    else:
        dp[1] = (stairs[0], stairs[0])
        dp[2] = (stairs[1], stairs[0]+stairs[1])
        # i번째 계단에 올라가는 방법은 1) i-2번째 계단에서 2계단 2) i-1번째 계단에서 1계단
        # dp[i]에 (1계단 연속인 경우, 2계단 연속인 경우)를 저장하여 3계단 연속 방지
        # 1) i-2에서 올라올 경우 3계단 연속을 생각하지 않아도 됨
        # 2) i-1에서 올라올 경우 1계단 연속인 경우만 가져올 수 있음
        for i in range(3, n+1):
            dp[i] = (max(dp[i-2])+stairs[i-1], dp[i-1][0]+stairs[i-1])
    return max(dp[n])


T = int(sys.stdin.readline())
stairs = []
for _ in range(T):
    stairs.append(int(sys.stdin.readline()))

print(get_stairs_sum(len(stairs)))