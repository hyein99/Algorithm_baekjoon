import sys
import heapq
input = sys.stdin.readline

INF = 1e9

# 입력
N, D = map(int, input().split())
graph = [[] for _ in range(D+1)]
for _ in range(N):
    s, e, l = map(int, input().split())
    if e > D:
        continue
    graph[s].append((e, l))  # graph[s] = (e, l): s > e 지름길 l

# 초기화
for i in range(D): # from i to i+1 거리를 1로 초기화
    graph[i].append((i+1, 1))
distance = [INF for _ in range(D+1)]

qu = []
heapq.heappush(qu, (0, 0))
distance[0] = 0
while qu:
    dist, node = heapq.heappop(qu)
    if distance[node] < dist:
        continue

    for n, d in graph[node]:
        if distance[n] > dist + d:
            distance[n] = dist + d
            heapq.heappush(qu, (distance[n], n))

print(distance[D])