# https://www.acmicpc.net/problem/17406

# 배열 A의 값: 각 행의 합 중 최솟값
# 회전(r, c, s)
# (r-s,c-s) ~ (r+s,c+s)정사각형을 시계 방향으로 한칸 돌리

import copy
from itertools import permutations

def rotate_arr(r, c, s):
    arr = [[(i, j) for j in range(M)] for i in range(N)]
    start, end = (r-s-1, c-s-1), (r+s-1, c+s-1)
    while start[0] <= end[0] and start[1] <= end[1]:
        # print(start, end)
        cur = start
        i, j = start[0], start[1]
        for d in dir:
            while start[0] <= i+d[0] <= end[0] and start[1] <= j+d[1] <= end[1]:
                ni, nj = i + d[0], j + d[1]
                # print(ni, nj)
                arr[ni][nj], cur = cur, arr[ni][nj]
                i, j = ni, nj

        start, end = (start[0]+1, start[1]+1), (end[0]-1, end[1]-1)

    return arr


# input
N, M, K = map(int, input().split())
origin = []
for _ in range(N):
    origin.append(list(map(int, input().split())))
rotate_list = []
rotate_dict = {}
dir = [(0,1), (1,0), (0,-1), (-1,0)]
for _ in range(K):
    r, c, s = map(int, input().split())
    rotate_list.append([r, c, s])
    # step 1: 회전 연산 미리 계산하기
    rotate_dict[(r, c, s)] = rotate_arr(r, c, s)

# step 2: 회전 연산 순서 정하기
result = int(1e9)
orders = permutations([i for i in range(K)], K)
for order in orders:
    # step 3: 회전 결과 (arr) 구하기
    rotated_arr = copy.deepcopy(origin)
    for o in order:
        r, c, s = rotate_list[o]
        # print(r, c, s)
        arr = rotate_dict[(r, c, s)]
        rotated_arr = [[rotated_arr[arr[i][j][0]][arr[i][j][1]] for j in range(M)] for i in range(N)]
        # print(*rotated_arr, sep='\n')

    # step 4: 배열 A의 값 구하기
    for i in range(N):
        result = min(result, sum(rotated_arr[i]))

print(result)