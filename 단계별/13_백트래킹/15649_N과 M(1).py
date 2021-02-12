# 리트코드 46(그래프-36_순열문제)

import sys
from collections import deque

# dfs: 재귀
def dfs():
    if len(result) == M:
        print(*result, sep=' ')
        return

    for i in range(1, N+1):
        if i in result:  # 중복 허용하지 않음
            continue
        result.append(i)
        # print(f'append {i}')
        dfs()            # len(result) == M일때까지 재귀
        result.pop()
        # print(f'pop {i}')


# version 1: itertools 사용
import itertools

def iter(N, M):
    num = [i+1 for i in range(N)]
    result = list(itertools.permutations(num, M))
    for r in result:
        print(*r, sep=' ')


N, M = map(int, sys.stdin.readline().split())   # 1부터 N까지 중 M개
result = deque()
dfs()