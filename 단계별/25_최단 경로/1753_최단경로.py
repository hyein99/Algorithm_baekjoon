import sys
from collections import defaultdict
import heapq

def get_dist(fr):
    Q = [[0, fr]] # 소요시간, 정점
    dist = defaultdict(int)

    while Q:
        time, node = heapq.heappop(Q)
        if node not in dist:
            dist[node] = time
            for v, w in graph[node]:
                heapq.heappush(Q, [time+w, v])
    return dist


# 입력
V, E = map(int, sys.stdin.readline().split()) # 정점개수, 간선개수
K = int(sys.stdin.readline())         # 시작점
graph = defaultdict(list)
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append([v, w]) # u에서 v까지 비용 w

# 출력
dist = get_dist(K)
for i in range(1, V+1):
    if i not in dist:
        print('INF')
    else:
        print(dist[i])