import sys

N, M = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
room = []
for _ in range(N):
    room.append(list(sys.stdin.readline().split()))

dir = [(-1,0), (0,1), (1,0), (0,-1)] # 0: 북, 1: 동, 2: 남, 3: 서
cnt = 0
dcnt = 0
while True:
    if room[r][c] == '0':
        room[r][c] = '#'
        cnt += 1
    if dcnt == 4: # 4번 돌아서 다시 원래대로
        back = [a+b for a, b in zip([r,c], dir[(d+2)%4])]
        if back[0]<0 or back[0]>=N or back[1]<0 or back[1]>=M \
                or room[back[0]][back[1]] == '1':
            break
        r = back[0]
        c = back[1]
        dcnt = 0

    left = [a+b for a, b in zip([r,c], dir[(d+4-1)%4])]
    if 0<=left[0]<N and 0<=left[1]<M and room[left[0]][left[1]] == '0': # 왼쪽 방향 청소 여부확인
        r = left[0]
        c = left[1]
        d = (d+4-1)%4
        dcnt = 0
    else:
        d = (d+4-1)%4
        dcnt += 1
print(cnt)

