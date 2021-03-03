import sys
from collections import defaultdict
import heapq

INF = sys.maxsize

def dijkstra(start):
    # 큐 변수
    Q = [[0, start]]
    dist = [INF for _ in range(N+1)]
    dist[start] = 0 ############ 시작점을 0으로

    while Q:
        time, node = heapq.heappop(Q)
        for v, w in graph[node]:
            if dist[v] > time+w:     # 다시 돌아 갈 순 있지만 짧을 때만
                dist[v] = time+w
                heapq.heappush(Q, [time+w, v])
    return dist

# 입력
N, E = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
v1, v2 = map(int, sys.stdin.readline().split())

from_one = dijkstra(1)
from_v1 = dijkstra(v1)
from_v2 = dijkstra(v2)

result = min(from_one[v1]+from_v1[v2]+from_v2[N], from_one[v2]+from_v2[v1]+from_v1[N])
if result >= INF:
    print(-1)
else:
    print(result)