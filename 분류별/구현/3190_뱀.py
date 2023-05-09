# https://www.acmicpc.net/problem/3190

from collections import deque

# 입력
N = int(input())
board = [[0 for _ in range(N)] for _ in range(N)]
K = int(input())
for _ in range(K):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1
L = int(input())
change = []
for _ in range(L):
    x, c = input().split()
    change.append((int(x), c))

result = 0           # 게임이 진행된 시간
i = 0                # i번째 뱀의 방향 변환 정보
cnt = change[i][0]   # 다음방향으로 바꾸기 까지 남은 초
dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
d = 0                # 현재 움직이는 방향
snake = deque()      # 현재 뱀의 위치 리스트
snake.append((0,0))
board[0][0] = -1     # 뱀이 위치하는 곳은 -1로 표시
while True:
    result += 1
    cnt -= 1
    head = snake[0]
    nx, ny = head[0]+dir[d][0], head[1]+dir[d][1]  # 몸길이를 방향(d)로 늘임
    # 벽이거나 몸에 부딪히면 종료
    if nx<0 or nx>=N or ny<0 or ny>=N or board[nx][ny] == -1:
        break

    snake.appendleft((nx, ny))  # 뱀의 머리 부분
    # 이동한 곳에 사과(1) 없으면 꼬리 0으로 바꾸기
    if board[nx][ny] != 1:
        tail = snake.pop()
        board[tail[0]][tail[1]] = 0
    board[nx][ny] = -1

    if cnt < 1:
        if change[i][1] == 'D':
            d = (d+1)%4
        else:
            d = (d+3)%4
        i += 1
        if i >= len(change):      # 마지막 방향 변환일 경우 무한대로
            cnt = N*N
        else:
            cnt = change[i][0]
            cnt -= change[i-1][0]

print(result)