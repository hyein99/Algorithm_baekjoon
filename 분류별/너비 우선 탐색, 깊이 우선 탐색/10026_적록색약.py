import sys
from collections import deque

def bfs(i, j):
    qu = deque()
    qu.append((i, j))
    color = board[i][j]
    done[i][j] = 0 # 방문 표시
    ### popleft()에서 방문체크를 하면 중복해서 방문체크함

    while qu:
        x, y = qu.popleft()
        for d in dir:
            nx, ny = x+d[0], y+d[1]
            if 0<=nx<N and 0<=ny<N and done[nx][ny]: # board 범위 안
                if board[nx][ny] == color:
                    done[nx][ny] = 0
                    qu.append((nx, ny))


# 입력
N = int(sys.stdin.readline())
board = []
for _ in range(N):
    board.append(list(sys.stdin.readline().rstrip()))
dir = [(-1,0), (1,0), (0,-1), (0,1)]

# 적록색약이 아닌 사람, 적록색약인 사람의 구역 수 구하기
RGB = 0
done = [[1] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if done[i][j]:
            bfs(i, j)
            RGB += 1
        if board[i][j] == 'G':
            board[i][j] = 'R'
RB = 0
done = [[1] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if done[i][j]:
            bfs(i, j)
            RB += 1

print(RGB, RB)
