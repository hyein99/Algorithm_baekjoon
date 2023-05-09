from collections import defaultdict


# 주사위를 굴려 next_value를 변환시키는 함수
def roll_dice(order):
    if order == 1:  # 동쪽: 윗면, 동, 서, 밑면 변화
        dice[1], dice[2], dice[3], dice[6] = dice[2], dice[6], dice[1], dice[3]
    elif order == 2:  # 서쪽: 윗면, 동, 서, 밑면 변화
        dice[1], dice[2], dice[3], dice[6] = dice[3], dice[1], dice[6], dice[2]
    elif order == 3:  # 북쪽: 윗면, 북, 남, 밑면 변화
        dice[1], dice[4], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[4]
    else:  # 남쪽: 윗면, 북, 남, 밑면 변화
        dice[1], dice[4], dice[5], dice[6] = dice[4], dice[6], dice[1], dice[5]


# 주사위를 이동시키고 주사위 값과 지도칸을 바꾸는 함수
def move_dice(order):
    global x, y

    # step 1) 주사위 이동
    nx, ny = x + dir[order][0], y + dir[order][1]
    if 0 <= nx < N and 0 <= ny < M:
        x, y = nx, ny
    else:
        return

    # step 2) 주사위 굴리기
    roll_dice(order)

    # step 3) 주사위 밑면과 지도 칸 값 바꾸기
    if amap[x][y] == 0:
        amap[x][y] = dice[6]
    else:
        dice[6] = amap[x][y]
        amap[x][y] = 0

    # step 4) 주사위 윗면 값 출력
    print(dice[1])


# 입력
N, M, x, y, K = map(int, input().split())
amap = []
for _ in range(N):
    amap.append(list(map(int, input().split())))
move_list = list(map(int, input().split()))

# 초기값 및 변수 세팅
dice = defaultdict(int)  # 주사위에 적힌 값(1~6: 윗면/동/서/북/남/밑면)
dir = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)]  # 주사위 굴리는 방향값

for order in move_list:
    move_dice(order)