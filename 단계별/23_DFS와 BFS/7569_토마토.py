import sys
from collections import deque

# bfs: 큐 + daylist
def get_tomato(list, xtom):
    qu = deque()
    qu.extend(list)
    cnt = H*N*M - len(list) - xtom # 남은 토마토 개수

    day = 0
    while qu:
        v = qu.popleft()
        for d in dir:
            i = v[0]+d[0]
            j = v[1]+d[1]
            k = v[2]+d[2]
            # (i, j, k) = tuple(a+b for a, b in zip(v, d))
            if 0<=i<H and 0<=j<N and 0<=k<M and box[i][j][k]=='0':
                box[i][j][k] = '1'
                dlist[i][j][k] = dlist[v[0]][v[1]][v[2]] + 1
                day = dlist[i][j][k]
                qu.append((i,j,k))
                cnt -= 1
    if cnt == 0:
        return day # 마지막 day를 가져옴
    else:
        return -1



# 상자 받아오기
M, N, H = map(int, sys.stdin.readline().split())
box = []
for _ in range(H):
    tmp = []
    for _ in range(N):
        tmp.append(sys.stdin.readline().rstrip().split())
    box.append(tmp)
# print(box)

dir = [(0,0,1),(0,0,-1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0)]
dlist = [[[0]*M for _ in range(N)] for _ in range(H)]   # 토마토가 익는 day list
tom = []  # 처음에 토마토가 있는 위치
xtom = 0  # -1의 개수
for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == '1':
                tom.append((i,j,k))
            elif box[i][j][k] == '-1':
                xtom += 1

print(get_tomato(tom, xtom))