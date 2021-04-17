# https://www.acmicpc.net/problem/1654

import sys

# 풀이 3) Parametric Search
def cut(length):
    cnt = 0
    for l in lines:
        cnt += l // length

    return cnt

# 입력
K, N = map(int, sys.stdin.readline().split())
lines = [int(sys.stdin.readline()) for _ in range(K)]

min_len, max_len = 1, max(lines)
while min_len <= max_len:
    mid = min_len + (max_len - min_len)//2

    if cut(mid) < N:         # 랜선이 모자른 경우
        max_len = mid - 1    # 더 작게 잘라야 함
    else:
        min_len = mid + 1

print(max_len)


# 풀이 1) 완전탐색 > 시간초과
# # 입력
# K, N = map(int, sys.stdin.readline().split())
# lines = [int(sys.stdin.readline()) for _ in range(K)]

# length = sum(lines)//N
# while True:
#     cnt = 0
#     for l in lines:
#         cnt += l//length
#     if cnt == N:
#         print(length)
#         break
#     length -= 1


# 풀이 2) Parametric Search - min/max 헷갈림
# def cut(length):
#     cnt = 0
#     for l in lines:
#         cnt += l // length

#     return cnt

# # 입력
# K, N = map(int, sys.stdin.readline().split())
# max_line = 0
# lines = []
# for _ in range(K):
#     n = int(sys.stdin.readline())
#     lines.append(n)
#     max_line = max(n, max_line)

# min_len = max_line//N
# max_len = sum(lines)//N
# while max_len - min_len > 1:
#     mid = min_len + (max_len - min_len)//2

#     cnt = cut(mid)
#     if cnt < N:            # 랜선이 모자른 경우
#         max_len = mid - 1  # 더 작게 잘라야 함
#     # 실패 원인????????????????????
#     # elif cnt > N:          # 랜선이 남는 경우
#     #     min_len = mid + 1  # 더 크게 잘라야 함
#     else:                  # 랜선이 N과 같은 경우
#         min_len = mid      # 더 크게 잘라야 함

# if cut(max_len) >= N:
#     print(max_len)
# else:
#     print(min_len)

