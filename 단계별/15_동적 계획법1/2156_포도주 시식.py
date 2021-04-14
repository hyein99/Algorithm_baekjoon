# 규칙에 따라 포도주를 마실 때, 최대로 마실 수 있는 포도주의 양을 구하는 문제
# max(dp[i-1], dp[i-3]+wine[i-2]+wine[i], dp[i-2]+wine[i])

import sys
from collections import defaultdict

def drink_wine(wine):
    if len(wine)<=2:
        return sum(wine)
    dp = defaultdict()
    dp[1] = (wine[0], wine[0])
    dp[2] = (max(wine[0], wine[1]), wine[0]+wine[1]) # (연속1, 연속2)
    for i in range(3, len(wine)+1):
        dp[i] = (max(max(dp[i-1]), dp[i-2][1]+wine[i-1]),
                 max(max(dp[i-1]), dp[i-1][0]+wine[i-1]))
    # print(dp)
    return dp[len(wine)][1]

# 입력
n = int(sys.stdin.readline())
wine = []
for _ in range(n):
    wine.append(int(sys.stdin.readline()))

print(drink_wine(wine))