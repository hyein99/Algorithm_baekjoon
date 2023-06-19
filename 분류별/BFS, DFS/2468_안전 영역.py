import sys
from collections import deque

def bfs(rain, i, j):
    qu = deque()
    qu.append((i, j))
    done[i][j] = 1

    while qu:
        x, y = qu.popleft()
        for d in dir:
            nx, ny = x+d[0], y+d[1]
            if 0<=nx<N and 0<=ny<N and not done[nx][ny]:
                if ground[nx][ny] > rain:
                    qu.append((nx, ny))
                    done[nx][ny] = 1


# 입력
N = int(sys.stdin.readline())
ground = []
for _ in range(N):
    ground.append(list(map(int, sys.stdin.readline().split())))

# 장마 높이별 안전지역 개수 구하기
rain = 0
max_safe = 0
dir = [(1,0), (-1,0), (0,1), (0,-1)]
while True:
    cnt = 0
    done = [[0]*N for _ in range(N)] # 방문여부
    for i in range(N):
        for j in range(N):
            if not done[i][j] and ground[i][j] > rain:
                bfs(rain, i, j)
                cnt += 1
    if cnt < 1:
        break
    max_safe = max(max_safe, cnt)
    rain += 1
print(max_safe)