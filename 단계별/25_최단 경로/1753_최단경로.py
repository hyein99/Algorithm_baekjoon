import sys
from collections import defaultdict
import heapq

INF = sys.maxsize
def get_dist(start):
    Q = []
    heapq.heappush(Q, (0, start))  # 소요시간, 정점
    dist = [INF]*(V+1)
    dist[start] = 0

    while Q:
        time, node = heapq.heappop(Q)

        ## 다익스트라 핵심 *****
        if dist[node] < time:
            continue

        for v, w in graph[node]:
            if dist[v] > time+w:
                heapq.heappush(Q, (time+w, v))
                dist[v] = time+w
    return dist


# 입력
V, E = map(int, sys.stdin.readline().split()) # 정점개수, 간선개수
K = int(sys.stdin.readline())                 # 시작점
graph = defaultdict(list)
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append([v, w]) # u에서 v까지 비용 w

# 출력
dist = get_dist(K)
for i in range(1, V+1):
    if dist[i] == INF:
        print('INF')
    else:
        print(dist[i])