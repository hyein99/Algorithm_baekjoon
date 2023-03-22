from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline
INF = 1e9

# 입력
V, E = map(int, input().split())
start = int(input())
graph = defaultdict(list)
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

qu = []
heapq.heappush(qu, (0, start))  # (거리, 노드)
distances = [INF for _ in range(V+1)]
distances[start] = 0
while qu:
    cost, node = heapq.heappop(qu)
    if distances[node] < cost:
        continue

    for (v, w) in graph[node]:
        if distances[v] > cost + w:
            distances[v] = cost + w
            heapq.heappush(qu, (cost+w, v))

# 출력
for i in range(1, V+1):
    if distances[i] >= INF:
        print('INF')
    else:
        print(distances[i])