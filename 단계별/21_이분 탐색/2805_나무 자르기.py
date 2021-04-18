# https://www.acmicpc.net/problem/2805
# PyPy3, python

import sys

def cut(height):
    result = 0
    for t in trees:
        if t > height:
            result += t-height
        # result += max(t-height, 0) ### >> python 시간초과
    return result

# 입력
N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))  # sort사용하는 것이 더 효율적

min_height = 0
max_height = max(trees) - 1   # M >= 1
while min_height <= max_height:
    mid = min_height + (max_height - min_height)//2
    if cut(mid) < M:          # 더 잘라야 함
        max_height = mid - 1
    else:
        min_height = mid + 1

print(max_height)

# if cut(max_height) >= M:
#     print(max_height)
# else:
#     print(min_height)