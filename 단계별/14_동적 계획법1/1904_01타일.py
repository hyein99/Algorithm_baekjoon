# n=1: 1(1)
# n=2: 2(11, 00)
# n=3: 3(111, 100, 001)
# n=4: 5(1111, 1100, 1001, 0011, 0000)
# n=5: 8(11111, 11100, 11001, 10011, 10000, 00111, 00100, 00001)

import sys

N = int(sys.stdin.readline())
dp = [0]*(N+2)
dp[1] = 1
dp[2] = 2
for i in range(3, N+1):
    dp[i] = (dp[i-1]+dp[i-2])%15746  # 나머지한 결과를 넣어줘서 메모리 초과를 방지함
print(dp[N])


def tile(N):
    x, y = 1, 2
    for _ in range(1, N):
        x, y = y, (x+y)%15746
    return x

N = int(sys.stdin.readline())
print(tile(N))