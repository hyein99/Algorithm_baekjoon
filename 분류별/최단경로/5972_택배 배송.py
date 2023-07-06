# 1 >> N
# 만나는 모든 소에게 여물
# 최소한 의 소 만나기
# 하나 이상의 길로 연결
# 양방향

from collections import defaultdict
import heapq

def dijkstra(start):
    h = []
    heapq.heappush(h, (0, start))
    cost = [int(1e9)] * (N+1)
    cost[start] = 0

    while h:
        c, now = heapq.heappop(h)
        if cost[now] < c:
            continue

        for b in graph[now]:
            if cost[b] > c + graph[now][b]:
                cost[b] = c + graph[now][b]
                heapq.heappush(h, (cost[b], b))

    return cost[N]


# input
N, M = map(int, input().split())
graph = defaultdict(lambda: {})
for _ in range(M):
    a, b, c = map(int, input().split())  # a-b 길에 c마리의 소
    if b in graph[a]:
        graph[a][b] = min(graph[a][b], c)
        graph[b][a] = min(graph[b][a], c)
    else:
        graph[a][b] = c
        graph[b][a] = c

print(dijkstra(1))
