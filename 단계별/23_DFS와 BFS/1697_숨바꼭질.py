# BFS 최단거리 문제

import sys

N, K = map(int, sys.stdin.readline().split())

cnt = 0
while cnt < 4:
    if 2*N <= K:
        N *= 2
    else:
        N -= 1
    cnt += 1
    print(cnt, N)

print(cnt)