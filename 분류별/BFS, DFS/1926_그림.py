from collections import deque

def BFS(i, j):
    qu = deque([(i, j)])
    paint[i][j] = '0'
    pcnt = 1
    while qu:
        x, y = qu.popleft()
        for d in dir:
            nx, ny = x+d[0], y+d[1]
            if 0<=nx<n and 0<=ny<m and paint[nx][ny] == '1':
                paint[nx][ny] = '0'
                qu.append((nx, ny))
                pcnt += 1
    return pcnt


# input
n, m = map(int, input().split())
paint = []
for _ in range(n):
    paint.append(input().split())

dir = [(1,0), (-1,0), (0,1), (0,-1)]
cnt = 0
max_paint = 0
for i in range(n):
    for j in range(m):
        if paint[i][j] == '1':
            cnt += 1
            max_paint = max(max_paint, BFS(i, j))


# output
print(cnt)
print(max_paint)