def turn(n, d):
    if d == 1:  # 시계방향
        top[n] = (top[n]+7)%8
    else:       # 반시계방향
        top[n] = (top[n]+1)%8


def get_tlist(n, d):
    arr = [(n, d)]

    # 회전하는 톱니바퀴 왼쪽에서 찾기
    cur_n, cur_d = n, d
    while cur_n-1 >= 0:
        # 극이 다르면 같이 회전
        if wheel[cur_n][(top[cur_n]+6)%8] == wheel[cur_n-1][(top[cur_n-1]+2)%8]:
            break
        arr.append((cur_n-1, -cur_d))
        cur_n -= 1
        cur_d *= (-1)

    # 회전하는 톱니바퀴 오쪽에서 찾기
    cur_n, cur_d = n, d
    while cur_n+1 < 4:
        # 극이 다르면 같이 회전
        if wheel[cur_n][(top[cur_n]+2)%8] == wheel[cur_n+1][(top[cur_n+1]+6)%8]:
            break
        arr.append((cur_n+1, -cur_d))
        cur_n += 1
        cur_d *= (-1)

    return arr


# 입력
wheel = []          # 0: N, 1: S
for _ in range(4):
    wheel.append(list(map(int, list(input()))))
K = int(input())    # 회전 수
top = [0, 0, 0, 0]  # i번째 톱니바퀴의 12시방향에 있는 순번
for _ in range(K):
    num, direction = map(int, input().split())
    turn_list = get_tlist(num-1, direction)    # 함께 돌아가는 (톱니, 방향)리스트
    for (n, d) in turn_list:
        turn(n, d)  # num번째 톱니바퀴, d방향(1: 시계, -1: 반시계)

# 점수 계산
score = 0
for i in range(4):
    if wheel[i][top[i]] == 1:
        score += 2**i
print(score)