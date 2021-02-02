# DFS: 깊이우선탐색
# BFS: 넓이우선탐색

import sys
from collections import deque

# 그래프 받아오기
N, M, V = sys.stdin.readline().split()
route = {}   # 그래프 보관할 dic
for _ in range(int(M)):
    a, b = sys.stdin.readline().split()
    if a in route:
        route[a].append(b)
    else:
        route[a] = [b]
    if b in route:
        route[b].append(a)
    else:
        route[b] = [a]
route = sorted(route.values())
print(route)

# DFS
# qu = deque()    # 앞으로 방문할 곳
# done = set()    # 이미 방문한 곳
# qu.append(V)
# done.add(V)
#
# while qu:
#     p = qu.popleft()
#     print(p, end=' ')
#     for v in route[p]:
#         # print(v)
#         if v not in done:
#             qu.append(v)
#             done.add(v)
