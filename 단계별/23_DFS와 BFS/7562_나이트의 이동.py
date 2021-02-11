import sys
from collections import deque

# bfs: 큐
def move_night(I, start, end):
    chess = [[0]*I for _ in range(I)]
    qu = deque()
    qu.append(start)

    while qu:
        v = qu.popleft()
        if v == end:
            return chess[v[0]][v[1]]
        for d in dir:
            i = v[0]+d[0]
            j = v[1]+d[1]
            # (i, j) = tuple(a+b for a, b in zip(v, d))
            if 0<=i<I and 0<=j<I and chess[i][j] == 0:
                qu.append((i,j))
                chess[i][j] = chess[v[0]][v[1]] + 1


T = int(sys.stdin.readline())
dir = [(1,2), (2,1), (2,-1), (1,-2), (-1,-2), (-2,-1), (-2,1), (-1,2)]

for _ in range(T):
    I = int(sys.stdin.readline())
    start = tuple(map(int, sys.stdin.readline().split()))
    end = tuple(map(int, sys.stdin.readline().split()))
    print(move_night(I, start, end))