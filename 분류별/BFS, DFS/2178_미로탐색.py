from collections import deque


def bfs(startx, starty):
    qu = deque()
    qu.append((startx, starty))

    while qu:
        x, y = qu.popleft()
        for d in dir:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] > 0:
                if graph[nx][ny] == 1: # not visited
                    graph[nx][ny] = graph[x][y] + 1
                    qu.append((nx, ny))


# 입력
N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, list(input()))))

dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
bfs(0, 0)
print(graph[N - 1][M - 1])
