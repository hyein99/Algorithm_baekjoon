import sys
from collections import deque

# bfs: 큐 활용: 시간초과
def count_maze(start):
    qu = deque()       # 앞으로 탐색할 경로
    qu.append(start)   # start:원점  # [start]로 하면 type(x) tuple 안해도됨

    while qu:
        # print(f'qu: {qu}')
        x = qu.popleft()
        p = [x] if type(x) is tuple else x    # 길이가 1이면 튜플 상태라서 p[-1]할 수 없음
        # print(f'p: {p}')
        v = p[-1]
        # print(f'v: {v}')
        if v == (N-1, M-1):   # 도착지점
            # print('answer: ', p)
            return len(p)

        pflag = False
        for d in dir:
            (i, j) = tuple(a+b for a, b in zip(v, d))
            # print(f'd: {d}, i: {i}, j: {j}')
            if 0<=i<N and 0<=j<M and maze[i][j]=='1'and (i,j) not in p:
                if pflag:       # p에 append되었음
                    p = p[:-1]
                p.append((i, j))
                qu.append(p)
                pflag = True


# bfs: 큐 사용 + 거리 list
def count_maze_bfs(start):
    qu = deque()       # 앞으로 탐색할 경로
    qu.append(start)   # start:원점

    while qu:
        v = qu.popleft()
        if v == (N-1, M-1):   # 도착지점
            # print('answer: ', p)
            print(dis)
            return dis[N-1][M-1]

        for d in dir:
            (i, j) = tuple(a+b for a, b in zip(v, d))  # 함수 만들어서 간단하게
            if 0<=i<N and 0<=j<M and maze[i][j]=='1':
                maze[i][j] = '0'
                dis[i][j] = dis[v[0]][v[1]] + 1
                qu.append((i,j))


# 미로 받아오기
N, M = map(int, sys.stdin.readline().split())
maze = []
for _ in range(N):
    maze.append(list(sys.stdin.readline().rstrip()))
# print(maze)

dir = [(0,1),(0,-1),(1,0),(-1,0)]
dis = [[1]*M for _ in range(N)]
# dis2 = [[0]*M for _ in range(N)]
print(count_maze_bfs((0,0)))
