import sys
from collections import deque

# bfs: 큐 + daylist
def get_tomato(list, xtom):
    qu = deque()
    qu.extend(list)
    cnt = N*M - len(list) - xtom # 남은 토마토 개수

    day = 0
    while qu:
        # print(f'qu: {qu}')
        v = qu.popleft()
        # print(f'v: {v}')
        for d in dir:
            (i, j) = tuple(a+b for a, b in zip(v, d))
            # print(f'(i,j): ({i},{j})')
            if 0<=i<N and 0<=j<M and box[i][j]=='0':
                box[i][j] = '1'
                dlist[i][j] = dlist[v[0]][v[1]] + 1
                day = dlist[i][j]
                qu.append((i,j))
                cnt -= 1
    if cnt == 0:
        return day # 마지막 day를 가져옴
    else:
        return -1


# 상자 받아오기
M, N = map(int, sys.stdin.readline().split())
box = []
for _ in range(N):
    box.append(sys.stdin.readline().rstrip().split())
# print(box)

dir = [(0,1),(0,-1),(1,0),(-1,0)]
dlist = [[0]*M for _ in range(N)] # 토마토가 익는 day list
tom = [] # 처음에 토마토가 있는 위치
xtom = 0 # -1의 개수
for i in range(N):
    for j in range(M):
        if box[i][j] == '1':
            tom.append((i,j))
        elif box[i][j] == '-1':
            xtom += 1
# print(tom)
print(get_tomato(tom, xtom))