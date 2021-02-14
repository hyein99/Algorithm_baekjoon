# BFS 최단거리 문제

import sys
from collections import deque

def find_sister(N, K):
    leng = max(N,K)*2
    road = [0 for _ in range(leng)] ###### 80%에서 런타임에러 >> 해결(0,0) ****
    # road = [0 for _ in range(100001)]
    qu = deque()
    qu.append(N)
    road[N] = 1 ## 60%에서 틀렸습니다

    while qu:
        v = qu.popleft()
        if v == K:
            return road[v]-1
        for i in range(3):
            if i == 0:
                x = v*2
            elif i == 1:
                x = v-1
            else:
                x = v+1
            # if 0<=x<100001 and road[x]==0:
            if 0<=x<leng and road[x]==0:
                qu.append(x)
                road[x] = road[v]+1


N, K = map(int, sys.stdin.readline().split())
print(find_sister(N, K))
