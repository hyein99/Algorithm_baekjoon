from collections import defaultdict

def operate_r(row, col):
    # 모든 행에 대해 정렬 시행
    for i in range(row):
        # i번째 행의 등장 횟수 구하기
        cnt_dict = defaultdict(int)
        for j in range(col):
            if arr[i][j] == 0:
                continue
            cnt_dict[arr[i][j]] += 1
            arr[i][j] = 0
        cnt_dict = sorted(cnt_dict.items(), key=lambda x: (x[1], x[0]))

        # i번째 행 재정렬
        idx = 0
        for cnt in cnt_dict:
            for c in cnt:
                arr[i][idx] = c
                idx += 1

            if idx >= 100:  # 100번째 넘어가는 경우 나머지 버림
                break

        # 증가한 col 계산
        col = max(col, len(cnt_dict) * 2)

    return row, col


def operate_c(row, col):
    # 모든 열에 대해 정렬 시행
    for i in range(col):
        # i번째 열의 등장 횟수 구하기
        cnt_dict = defaultdict(int)
        for j in range(row):
            if arr[j][i] == 0:
                continue
            cnt_dict[arr[j][i]] += 1
            arr[j][i] = 0
        cnt_dict = sorted(cnt_dict.items(), key=lambda x: (x[1], x[0]))

        # i번째 열 재정렬
        idx = 0
        for cnt in cnt_dict:
            for c in cnt:
                arr[idx][i] = c
                idx += 1

            if idx >= 100:  # 100번째 넘어가는 경우 나머지 버림
                break

        # 증가한 col 계산
        row = max(row, len(cnt_dict) * 2)

    return row, col

# input
R, C, K = map(int, input().split())
arr = [[0]*100 for _ in range(100)]
for i in range(3):
    arr[i][0], arr[i][1], arr[i][2] = map(int, input().split())

time_cnt = 0
row, col = 3, 3
while arr[R-1][C-1] != K:
    if time_cnt >= 100:
        time_cnt = -1
        break

    if row >= col:
        # R 연산
        row, col = operate_r(row, col)
    else:
        row, col = operate_c(row, col)
    time_cnt += 1

print(time_cnt)