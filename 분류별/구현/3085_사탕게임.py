import copy
from collections import deque

def countLongest(i, j):
    c = boardcopy[i][j]
    boardcopy[i][j] = 'X'  # 방문표시
    qu = deque()
    qu.append((i, j))
    cnt = 1
    while qu:
        x, y = qu.popleft()
        for d in dir:
            nx, ny = x + d[0], y + d[1]
            if 0<=nx<N and 0<=ny<N and boardcopy[nx][ny] == c:
                qu.append((nx, ny))
                boardcopy[nx][ny] = 'X'
                cnt += 1

    return cnt


# 입력
N = int(input())
board = []
for _ in range(N):
    board.append(list(input()))

dir = [(0,1), (1,0), (0,-1), (-1,0)]
answer = 0
# stage 1: 사탕의 색이 다른 서로 다른 인접 두 칸 고르기
for i1 in range(N):
    for j1 in range(N):
        for d in dir[:2]:  # 앞에서 본 조합 중복 안되기 위해
            i2, j2 = i1 + d[0], j1 + d[1]
            if 0<=i2<N and 0<=j2<N and board[i1][j1] != board[i2][j2]:
                boardcopy = copy.deepcopy(board)
                # stage 2: 두 개 교환
                boardcopy[i1][j1], boardcopy[i2][j2] = boardcopy[i2][j2], boardcopy[i1][j1]

                # stage 3: 모두 같은 색으로 되어 있는 가장 긴 연속 부분 찾기
                for x in range(N):
                    for y in range(N):
                        if boardcopy[x][y] != 'X':
                            answer = max(answer, countLongest(x, y))
                            print(*boardcopy, sep='\n')

print(answer)