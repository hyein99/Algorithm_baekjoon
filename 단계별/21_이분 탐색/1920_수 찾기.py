# https://www.acmicpc.net/problem/1920

import sys

# 입력
N = int(sys.stdin.readline())
arr1 = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
arr2 = list(map(int, sys.stdin.readline().split()))

# 풀이 1) 둘다 정렬(X) arr2를 정렬하면 순서대로 출력 못함
# arr1.sort()
# arr2.sort()
# idx1 = 0
# for idx2 in range(M):
#     while True:
#         if idx1 >= N or arr1[idx1] > arr2[idx2]:
#             print(0)
#             break
#         elif arr1[idx1] < arr2[idx2]:
#             idx1 += 1
#         else:
#             print(1)
#             break

# 풀이 2) arr1만 정렬하고 이진 탐색
def bin_search(target):
    left, right = 0, len(arr1)-1
    while left <= right:
        mid = left + (right-left)//2

        if arr1[mid] < target:
            left = mid + 1
        elif arr1[mid] > target:
            right = mid - 1
        else:
            return 1
    return 0

arr1.sort()
for n in arr2:
    print(bin_search(n))