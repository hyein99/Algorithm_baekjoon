import sys
from collections import deque

# dfs: 재귀
def dfs():
    if len(result) == M:
        print(*result, sep=' ')
        return

    for i in range(1, N+1):
        result.append(i)
        dfs()            # len(result) == M일때까지 재귀
        result.pop()

N, M = map(int, sys.stdin.readline().split())   # 1부터 N까지 중 M개
result = deque()
dfs()