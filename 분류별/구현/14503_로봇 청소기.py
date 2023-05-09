# import sys
#
# N, M = map(int, sys.stdin.readline().split())
# r, c, d = map(int, sys.stdin.readline().split())
# room = []
# for _ in range(N):
#     room.append(list(sys.stdin.readline().split()))
#
# dir = [(-1,0), (0,1), (1,0), (0,-1)] # 0: 북, 1: 동, 2: 남, 3: 서
# cnt = 0
# dcnt = 0
# while True:
#     if room[r][c] == '0':
#         room[r][c] = '#'
#         cnt += 1
#     if dcnt == 4: # 4번 돌아서 다시 원래대로
#         back = [a+b for a, b in zip([r,c], dir[(d+2)%4])]
#         if back[0]<0 or back[0]>=N or back[1]<0 or back[1]>=M \
#                 or room[back[0]][back[1]] == '1':
#             break
#         r = back[0]
#         c = back[1]
#         dcnt = 0
#
#     left = [a+b for a, b in zip([r,c], dir[(d+4-1)%4])]
#     if 0<=left[0]<N and 0<=left[1]<M and room[left[0]][left[1]] == '0': # 왼쪽 방향 청소 여부확인
#         r = left[0]
#         c = left[1]
#         d = (d+4-1)%4
#         dcnt = 0
#     else:
#         d = (d+4-1)%4
#         dcnt += 1
# print(cnt)
#

N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = []
for _ in range(N):
    room.append(list(map(int, input().split()))) # 0: 빈칸, 1: 벽
dir = [(-1,0),(0,1),(1,0),(0,-1)]  # 북동남서

answer = 0
cnt = 0
while True:
    # step 1: 현재 칸 청소
    if room[r][c] == 0:
        room[r][c] = 2
        answer += 1
    else:
        # step 3: 4칸 중 청소되지 않은 빈칸이 없는 경우
        if cnt == 4:
            nr, nc = r + dir[(d + 2) % 4][0], c + dir[(d + 2) % 4][1]
            if room[nr][nc] == 1:
                break
            else:
                r, c = nr, nc
                cnt = 0
                continue

        # step 2: 반시계 90도 회전
        d = (d+3)%4
        nr, nc = r + dir[d][0], c + dir[d][1]
        if room[nr][nc] == 0:
            r, c = nr, nc
            cnt = 0
        else:
            cnt += 1


print(answer)




