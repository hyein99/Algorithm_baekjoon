import sys

def coin(N, K):
    cnt = 0
    while K != 0:
        if money[N-1] <= K:
            cnt += K // money[N-1]
            K = K % money[N-1]
        N -= 1

    return cnt

# 입력
N, K = map(int, sys.stdin.readline().split())
money = []
for _ in range(N):
    money.append(int(sys.stdin.readline()))

print(coin(N, K))