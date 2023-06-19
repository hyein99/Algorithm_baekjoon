import sys
from collections import deque

def bfs(i, j):
    qu = deque()
    qu.append([i, j])
    paper[i][j] = '#'

    cnt = 1
    while qu:
        v = qu.popleft()
        for d in dir:
            nx, ny = v[0]+d[0], v[1]+d[1]
            if 0<=nx<M and 0<=ny<N and not paper[nx][ny]:
                qu.append([nx, ny])
                paper[nx][ny] = '#'
                cnt += 1

    return cnt


def dfs(i, j):
    st = deque()
    st.append([i, j])

    cnt = 1
    while st:
        v = st.pop()
        paper[i][j] = '#'
        for d in dir:
            nx, ny = v[0]+d[0], v[1]+d[1]
            if 0<=nx<M and 0<=ny<N and not paper[nx][ny]:
                st.append([nx, ny])
                paper[nx][ny] = '#'
                cnt += 1

    return cnt


M, N, K = map(int, sys.stdin.readline().split())
paper = [[0]*N for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            paper[i][j] = 1

cntlist = []
dir = [(1,0), (-1,0), (0,1), (0,-1)]
for i in range(M):
    for j in range(N):
        if not paper[i][j]:
            cntlist.append(dfs(i, j))

print(len(cntlist))
print(*sorted(cntlist))