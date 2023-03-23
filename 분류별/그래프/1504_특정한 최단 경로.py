# ================== case 1: 플루이드 워셜: 시간초과

# import sys
# input = sys.stdin.readline
# INF = int(1e9)

# # 입력
# N, E = map(int, input().split())
# distance = [[INF] * (N+1) for _ in range(N+1)]
# for i in range(1, N+1):  # 자기자신 초기화
#     distance[i][i] = 0
# for _ in range(E):
#     a, b, c = map(int, input().split())
#     distance[a][b] = c
#     distance[b][a] = c
# v1, v2 = map(int, input().split())
#
# for k in range(1, N+1):
#     for i in range(1, N+1):
#         for j in range(i+1, N+1):
#             if k == i or k == j:
#                 continue
#             dist = min(distance[i][j], distance[i][k]+distance[k][j])
#             distance[i][j] = dist
#             distance[j][i] = dist
#
# answer = min(distance[1][v1] + distance[v1][v2] + distance[v2][N], distance[1][v2] + distance[v2][v1] + distance[v1][N])
# if answer >= INF:
#     print(-1)
# else:
#     print(answer)


# ================== case 2: 다익스트라
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    qu = []
    heapq.heappush(qu, (0, start))
    distance = [INF for _ in range(N + 1)]
    distance[start] = 0
    while qu:
        dist, node = heapq.heappop(qu)
        if distance[node] < dist:
            continue

        for (n, d) in graph[node]:
            if distance[n] > dist + d:
                distance[n] = dist + d
                heapq.heappush(qu, (dist+d, n))
    return distance


# 입력
N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())

from_start = dijkstra(1)
from_v1 = dijkstra(v1)
from_v2 = dijkstra(v2)

answer = min(from_start[v1] + from_v1[v2] + from_v2[N], from_start[v2] + from_v2[v1] + from_v1[N])
if answer >= INF:
    print(-1)
else:
    print(answer)