# 카운팅 정렬

# def count_sort(arr):
#     minnum = min(arr)
#     narr = [0]*(max(arr) - minnum + 1)
#     for i in arr:
#         narr[i-minnum] += 1
#
#     idx = 0
#     for i in range(len(narr)):
#         while narr[i] > 0 :
#             arr[idx] = i + minnum
#             idx += 1
#             narr[i] -= 1

import sys

N = int(sys.stdin.readline())
nlist = [0]*10001
for _ in range(N):
    num = int(sys.stdin.readline())
    nlist[num] += 1
for i in range(len(nlist)):
    if nlist[i] != 0:
        for _ in range(nlist[i]):
            print(i)