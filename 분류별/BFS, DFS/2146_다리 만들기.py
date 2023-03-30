from collections import deque


def bfs_island(i, j, cnt):
    qu = deque()
    qu.append((i, j))
    graph[i][j] = cnt

    while qu:
        x, y = qu.popleft()
        for d in dir:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1:
                graph[nx][ny] = cnt
                qu.append((nx, ny))


def bfs_distance(num):
    qu = deque()
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if graph[i][j] == num:
                qu.append((i, j, 0))
                visited[i][j] = 1

    # print(num)
    # print(*visited, sep='\n')
    distance = N*N
    while qu:
        x, y, w = qu.popleft()
        for d in dir:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                visited[nx][ny] = 1
                if graph[nx][ny] == 0:
                    qu.append((nx, ny, w+1))
                else:  # 다른 섬 만남
                    distance = w
                    return distance
    return distance


# 입력
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# step 1) 섬 구분하기
cnt = 2  # 이미 1부터 시작해서
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            bfs_island(i, j, cnt)
            cnt += 1
# print(*graph, sep='\n')

# step 2) 최단 거리 구하기
answer = N*N
for num in range(2, cnt):
    dist = bfs_distance(num)
    # print(dist)
    answer = min(answer, dist)

print(answer)