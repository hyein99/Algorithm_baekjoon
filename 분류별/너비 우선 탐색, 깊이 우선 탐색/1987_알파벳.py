import sys
from collections import deque

"""
1) deque()로 했을 때 시간초과 > set()
2) max_len 은 1부터 시작!
"""

def bfs(i, j):
    max_len = 1
    # qu = deque()
    # qu.append((i, j, board[i][j]))
    qu = set([(i, j, board[i][j])])

    while qu:
        # x, y, alpha = qu.popleft()
        x, y, alpha = qu.pop()
        for d in dir:
            nx, ny = x+d[0], y+d[1]
            if 0<=nx<R and 0<=ny<C and board[nx][ny] not in alpha:
                # qu.append((nx, ny, alpha+board[nx][ny]))
                qu.add((nx, ny, alpha+board[nx][ny]))
                max_len = max(max_len, len(alpha)+1)
    return max_len


# 입력
R, C = map(int, sys.stdin.readline().split())
board = []
for _ in range(R):
    board.append(list(sys.stdin.readline().rstrip()))

# 출력
dir = [(1,0), (-1,0), (0,1), (0,-1)]
print(bfs(0,0))