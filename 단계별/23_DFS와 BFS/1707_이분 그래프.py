import sys
from collections import deque

def get_bigraph(graph, start):
    qu = deque()
    qu.append(start)

    bigraph[start] = True
    # print(f'bigraph: {bigraph}')
    while qu:
        v = qu.popleft()
        # print(f'v: {v}')
        for x in graph[v]:
            # print(f'x: {x}')
            if not visited[x]:
                bigraph[x] = not bigraph[v]
                qu.append(x)
                visited[x] = True
            elif bigraph[x] == bigraph[v]: # 이미 지나간 자리
                return False
            # print(f'bigraph: {bigraph}')
    return True


K = int(sys.stdin.readline())
for _ in range(K):
    V, E = map(int, sys.stdin.readline().split()) # 정점, 간선
    graph = [[] for i in range(V)] # V+1로 하는거 추천!!!!!
    for _ in range(E):
        x, y = map(int, sys.stdin.readline().split())
        graph[x-1].append(y-1)
        graph[y-1].append(x-1)

    bigraph = ['' for _ in range(len(graph))]     # 이분그래프    # 두 개 합치는 거 추천
    visited = [False for _ in range(len(graph))]  # 방문 여부
    result = True
    for n in range(V):             # 함수로 만드는 거 추천!!!!!
        if not visited[n]: # 아직 방문하지 않은 정점
            result = get_bigraph(graph, n)
            if not result:
                break
    print('YES') if result else print('NO')

