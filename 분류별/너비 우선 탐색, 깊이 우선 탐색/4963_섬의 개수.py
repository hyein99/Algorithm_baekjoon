import sys
from collections import deque

def bfs(i, j):
    qu = deque()
    qu.append([i, j])
    mplist[i][j] = '#'
    while qu:
        v = qu.popleft()
        for d in dir:
            nx, ny = v[0]+d[0], v[1]+d[1]
            if 0<=nx<h and 0<=ny<w and mplist[nx][ny]==1:
                qu.append([nx, ny])
                mplist[nx][ny] = '#'

# def bfs(i, j):
#     qu = deque()
#     qu.append([i, j])
#     while qu:
#         v = qu.popleft()
#         mplist[v[0]][v[1]] = '#'
#         for d in dir:
#             nx, ny = v[0]+d[0], v[1]+d[1]
#             if 0<=nx<h and 0<=ny<w and mplist[nx][ny]==1:
#                 qu.append([nx, ny])

def dfs(i, j):
    st = deque()
    st.append([i, j])
    while st:
        v = st.pop()
        mplist[v[0]][v[1]] = '#'
        for d in dir:
            nx, ny = v[0]+d[0], v[1]+d[1]
            if 0<=nx<h and 0<=ny<w and mplist[nx][ny]==1:
                st.append([nx, ny])
                mplist[nx][ny] = '#'


dir = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]
while True:
    w, h = map(int, sys.stdin.readline().split())
    if not w and not h:
        break
    mplist = []
    for _ in range(h):
        mplist.append(list(map(int, sys.stdin.readline().split())))

    cnt = 0
    for i in range(h):
        for j in range(w):
            if mplist[i][j]==1:
                dfs(i, j)
                cnt += 1
    print(cnt)