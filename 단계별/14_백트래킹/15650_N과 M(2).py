import sys
from collections import deque

# 풀이 1) dfs: 재귀 > 100ms
def dfs(self):
    if len(result) == M:
        print(*result)
        return

    for i in range(1, N+1):
        if i <= self:  # 중복 허용하지 않음
            continue
        result.append(i)
        dfs(i)            # len(result) == M일때까지 재귀
        result.pop()

# 풀이 2) dfs: 재귀 > 104ms
# def dfs(self):
#     if len(result) == M:
#         print(*result)
#         return
#
#     for i in range(self+1, N+1):
#         result.append(i)
#         dfs(i)            # len(result) == M일때까지 재귀
#         result.pop()

N, M = map(int, sys.stdin.readline().split())   # 1부터 N까지 중 M개
result = deque()
dfs(0)