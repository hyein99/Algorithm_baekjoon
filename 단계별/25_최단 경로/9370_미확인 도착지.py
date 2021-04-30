import sys
from collections import defaultdict
import heapq

INF = sys.maxsize
# 풀이 2) start-g-h-end, start-h-g-end 계산하는 방법
def dijkstra(start):
    # 큐 변수
    Q = [[0, start]]
    dist = [INF for _ in range(n + 1)]
    dist[start] = 0

    while Q:
        time, node, = heapq.heappop(Q)

        ## 다익스트라 핵심 *****
        if dist[node] < time:
            continue

        for v, w in graph[node]:
            if dist[v] > time + w:
                dist[v] = time + w
                heapq.heappush(Q, [time + w, v])

    return dist


T = int(sys.stdin.readline())
for _ in range(T):
    # 입력
    n, m, t = map(int, sys.stdin.readline().split())  # 교차로, 도로, 목적지 후보의 개수
    s, g, h = map(int, sys.stdin.readline().split())  # 출발지, 교차로 g-h
    graph = defaultdict(list)
    for _ in range(m):
        a, b, d = map(int, sys.stdin.readline().split())  # a와 b사이에 있는 도로 d
        graph[a].append([b, d])
        graph[b].append([a, d])

    # 다익스트라 계산 및 출력
    from_s = dijkstra(s)
    from_g = dijkstra(g)
    from_h = dijkstra(h)
    result = []
    for _ in range(t):
        c = int(sys.stdin.readline())  # 목적지 후보
        # print('최단거리', from_s[c])
        # print('g-h', from_s[g], from_g[h], from_h[c])
        # print('h-g', from_s[h], from_h[g], from_g[c])
        if from_s[c] == from_s[g] + from_g[h] + from_h[c]:  # c로 가는 최단거리일 경우
            result.append(c)
        elif from_s[c] == from_s[h] + from_h[g] + from_g[c]:
            result.append(c)

    result.sort()
    print(*result)



# 풀이 1) g-h구간 체크하는 방법 > 시간초과
# def dijkstra(s, g, h, cand):
#     # 큐 변수
#     Q = [[0, s, False]]
#     dist = defaultdict(int)
#     result = []
#
#     while Q:
#         time, node, check = heapq.heappop(Q)
#         if (node not in dist) or (dist[node]==time):  # 최단 경로가 여러가지 있을 수 있음
#             dist[node] = time
#             if cand[node] and check:     # 목적지 후보이고 check가 True이면
#                 result.append(node)      # 결과 리스트에 추가
#             for v, w in graph[node]:
#                 chk = check
#                 if (node==g and v==h) or (node==h and v==g): # g-h
#                     chk = True
#                 heapq.heappush(Q, [time+w, v, chk])
#
#     return sorted(result)
#
#
# T = int(sys.stdin.readline())
# for _ in range(T):
#     # 입력
#     n, m, t = map(int, sys.stdin.readline().split())
#     s, g, h = map(int, sys.stdin.readline().split())
#     graph = defaultdict(list)
#     for _ in range(m):
#         a, b, d = map(int, sys.stdin.readline().split())
#         graph[a].append([b, d])
#         graph[b].append([a, d])
#     cand = defaultdict(int)
#     for _ in range(t):
#         cand[int(sys.stdin.readline())] = 1
#
#     # 출력
#     result = dijkstra(s, g, h, cand)
#     print(*result)