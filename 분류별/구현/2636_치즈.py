import sys
from collections import deque
input = sys.stdin.readline

def bfs(i, j):
    qu = deque([(i, j)])
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[i][j] = 1
    ground[i][j] = -1
    while qu:
        x, y = qu.popleft()
        for d in dir:
            nx, ny = x+d[0], y+d[1]
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
                visited[nx][ny] = 1
                if ground[nx][ny] != 1:
                    qu.append((nx, ny))
                    ground[nx][ny] = -1


# input
N, M = map(int, input().split())
ground = []
for _ in range(N):
    ground.append(list(map(int, input().split())))
dir = [(1,0), (-1,0), (0,1), (0,-1)]

cheese_cnt = 0
for i in range(N):
    cheese_cnt += sum(ground[i])

outx, outy = 0, 0
time_cnt = 0
last_cnt = cheese_cnt
while cheese_cnt > 0:
    last_cnt = cheese_cnt

    # step 1: 외부 공기 표시(-1)
    bfs(outx, outy)

    # step 2: 실내온도 접촉한 칸 찾기
    melting = []
    for i in range(N):
        for j in range(M):
            if ground[i][j] == 1:
                for d in dir:
                    ni, nj = i+d[0], j+d[1]
                    if 0<=ni<N and 0<=nj<M and ground[ni][nj] == -1:
                        melting.append((i, j))
                        break

    # step 3: 치즈 녹기
    cheese_cnt -= len(melting)
    for (i, j) in melting:
        ground[i][j] = -1

    # print(*ground, sep='\n')
    # print(len(melting))
    if melting:
        outx, outy = melting[0]
    time_cnt += 1

# output
print(time_cnt)  # 치즈가 모두 녹는데 걸리는 시간
print(last_cnt)  # 마지막 한 시간 전에 남아있는 치즈 개수