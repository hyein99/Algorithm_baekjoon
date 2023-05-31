# https://www.acmicpc.net/problem/2116

# 주사위 1~6: 보통 주사위 아님 (마주보는 면 합 7 아님)
# 1 > 2 > 3 번 주사위 순서 쌓기
# 서로 붙어 있는 두개의 주사위에서 아래 주사위 윗면 = 위 주사위 아랫면
# 주사위 1 윗면 = 주사위 2 아랫면
# 주사위 1은 자유

# input
N = int(input())
dice_list = []
for _ in range(N):
    dice_list.append(list(map(int, input().split())))
updown = {0:5, 1:3, 2:4, 3:1, 4:2, 5:0}

max_dsum = 0
for n in range(1, 7):
    up = n
    dsum = 0
    for i in range(N):
        up_i = dice_list[i].index(up)
        down_i = updown[up_i]
        down = dice_list[i][down_i]
        dsum += max(set([1,2,3,4,5,6])-set([up, down]))

        up = down

    max_dsum = max(max_dsum, dsum)

print(max_dsum)