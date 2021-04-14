import sys
from collections import deque

# 풀이 1) dfs > 2160ms
# def dfs():
#     if len(result) == M:
#         print(*result)
#         return
#
#     for i in range(1, N+1):
#         result.append(i)
#         dfs()            # len(result) == M일때까지 재귀
#         result.pop()
#
# N, M = map(int, sys.stdin.readline().split())   # 1부터 N까지 중 M개
# result = deque()
# dfs()

# 풀이 2) dfs > 2020ms
def dfs(sub):
    if len(sub) == M:
        print(*sub)
        return

    for i in range(1, N+1):
        dfs(sub+[i])

N, M = map(int, sys.stdin.readline().split())   # 1부터 N까지 중 M개
dfs([])