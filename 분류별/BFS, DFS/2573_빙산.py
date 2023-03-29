from collections import deque
import copy


def bfs(i, j):
    qu = deque()
    qu.append((i, j))
    while qu:
        x, y = qu.popleft()
        for d in dir:
            nx, ny = x + d[0], y + d[1]
            if 0<=nx<N and 0<=ny<M and tmp_graph[nx][ny] > 0:
                tmp_graph[nx][ny] = 0
                qu.append((nx, ny))


def melt():
    # 녹아야 하는 양 계산
    melt_cnt = [[0] * M for _ in range(N)]
    for i in range(1, N-1):
        for j in range(1, M-1):
            cnt = 0
            for d in dir:
                ni, nj = i + d[0], j + d[1]
                if 0<=ni<N and 0<=nj<M and graph[ni][nj] == 0:
                    cnt += 1
            melt_cnt[i][j] = cnt

    # 녹은 양 만큼 제거
    for i in range(1, N-1):
        for j in range(1, M-1):
            graph[i][j] = max(0, graph[i][j] - melt_cnt[i][j])


# 입력
N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
answer = 0
while True:
    # step 1) 빙산 개수 > 2덩이 이상이면 종료
    bing_cnt, total = 0, 0
    tmp_graph = copy.deepcopy(graph)
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if tmp_graph[i][j] > 0:
                bfs(i, j)
                bing_cnt += 1
                total = 1
    if bing_cnt > 1:
        break
    elif total == 0:  # 빙산 다 녹았는데 2덩이 안되면 0
        answer = 0
        break
    # print(bing_cnt)

    # step 2) 빙산 녹기
    melt()
    # print(*graph, sep='\n')

    # step 3)
    answer += 1

print(answer)