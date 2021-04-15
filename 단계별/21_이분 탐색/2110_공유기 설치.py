# https://www.acmicpc.net/problem/2110

import sys

# 공유기 C개를 interval 이상의 간격으로 배치할 수 있는지 판단하는 함수
def put_router(interval):
    cnt = C
    prev_loc = -interval  # 첫번째 집에 무조건 공유기 설치하기 위해
    for h in house:
        if h - prev_loc >= interval:  # interval: 가장 인접한 거리
            cnt -= 1
            prev_loc = h

        # 마지막 공유기가 마지막 house에 위치하지 않았을 경우 상관 x?
        if cnt == 0:     # 공유기 C개 다 설치한 경우
            return True

    return False         # 공유기 C개 다 설치 못한 경우


# 입력
N, C = map(int, sys.stdin.readline().split())
house = sorted([int(sys.stdin.readline()) for _ in range(N)])

# 이분 탐색
min_interval = 0
max_interval = house[-1] - house[0]
while min_interval <= max_interval:
    mid = min_interval + (max_interval - min_interval)//2

    if put_router(mid):          # mid 간격으로 공유기 설치할 수 있으면
        min_interval = mid + 1   # 간격 넓힐 수 있음
    else:                        # mid 간격으로 공유기 설치하면 다 설치 못하는 경우
        max_interval = mid - 1   # 간격 줄여야 함

print(max_interval)
