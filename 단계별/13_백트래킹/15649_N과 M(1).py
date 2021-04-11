# 리트코드 46(그래프-36_순열문제)

import sys
from collections import deque

# 풀이 1) dfs > 288ms
# def dfs():
#     if len(result) == M:
#         print(*result)
#         return
#
#     for i in range(1, N+1):
#         if i in result:  # 중복 허용하지 않음
#             continue
#         result.append(i)
#         dfs()            # len(result) == M일때까지 재귀
#         result.pop()
#
# N, M = map(int, sys.stdin.readline().split())   # 1부터 N까지 중 M개
# used = [0]*M
# result = deque()
# dfs()

# 풀이 2) dfs > 276ms
# def dfs(sub):
#     if len(sub) == M:
#         print(*sub)
#         return
#     for i in range(1,N+1):
#         if used[i] == 0:
#             used[i] = 1
#             dfs(sub+[i])
#             used[i] = 0
#
# N, M = map(int, sys.stdin.readline().split())   # 1부터 N까지 중 M개
# used = [0]*(N+1)
# result = deque()
# dfs([])


# 풀이 3) itertools 사용 > 180ms
import itertools

def iter(N, M):
    num = [i+1 for i in range(N)]
    result = list(itertools.permutations(num, M))
    for r in result:
        print(*r)


N, M = map(int, sys.stdin.readline().split())   # 1부터 N까지 중 M개
iter(N, M)