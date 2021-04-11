import sys
from collections import deque

# dfs: 재귀
def dfs(self):
    if len(result) == M:
        print(*result)
        return

    for i in range(1, N+1):
        if i < self:  # 중복 허용하지 않음
            continue
        result.append(i)
        dfs(i)            # len(result) == M일때까지 재귀
        result.pop()

N, M = map(int, sys.stdin.readline().split())   # 1부터 N까지 중 M개
result = deque()
dfs(0)