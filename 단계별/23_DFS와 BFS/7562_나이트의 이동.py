import sys
from collections import deque

# bfs: 큐
def move_night(I, start, end):
    chess = [[0]*I for _ in range(I)]
    qu = deque()
    qu.append(start)

    while qu:
        x, y = qu.popleft()
        if (x, y) == end:
            return chess[x][y]
        for d in dir:
            nx, ny = x+d[0], y+d[1]
            if 0<=nx<I and 0<=ny<I and chess[nx][ny] == 0:
                qu.append((nx,ny))
                chess[nx][ny] = chess[x][y] + 1


T = int(sys.stdin.readline())
dir = [(1,2), (2,1), (2,-1), (1,-2), (-1,-2), (-2,-1), (-2,1), (-1,2)]

for _ in range(T):
    I = int(sys.stdin.readline())
    start = tuple(map(int, sys.stdin.readline().split()))
    end = tuple(map(int, sys.stdin.readline().split()))
    print(move_night(I, start, end))