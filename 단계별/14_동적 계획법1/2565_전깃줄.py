import sys
from collections import defaultdict

# def LIS(arr, maxn):
#     dp = []
#     dp.append([maxn, 0])
#     dp.append([arr[maxn]-1, 0])
#     l = 2 # 현재 선 개수+1
#     for i in range(maxn-1, 0, -1):
#         # print(i)
#         # print(dp)
#         if arr[i] == 0:            # 선이 없음
#             continue
#         elif arr[i] <= dp[l-1][0]: # 선이 안겹침
#             dp.append([arr[i]-1, dp[l-1][1]])
#             l += 1
#         else:                      # 선이 겹침
#             if dp[l-2][0] >= arr[i] and arr[i]-1 > dp[l-1][0]: # 이전 선 자르기
#                 dp.append([arr[i]-1, dp[l-1][1]+1])
#                 del dp[l-1]
#             else: # 현재 선 자르기
#                 dp[l-1][1] += 1
#
#     print(dp)
#     return dp[-1][1]

def LIS(arr):
    result = 1
    dp = [1 for _ in range(arr[0][0]+1)]
    # dp[i]: arr[i]를 마지막 원소로 가지는 부분수열의 길이
    for i in range(len(arr)):
        # print(i)
        # print(dp)
        for j in range(i):
            if arr[i][1] < arr[j][1] and dp[arr[i][0]] < dp[arr[j][0]]+1:
                dp[arr[i][0]] = dp[arr[j][0]]+1
                if dp[arr[i][0]] > result:
                    result = dp[arr[i][0]]

    return len(arr)-result

# 입력
N = int(sys.stdin.readline())
lines = defaultdict(int)
maxn = N
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    lines[x] = y
    if x > maxn:
        maxn = x

# print(LIS(lines, maxn))
print(LIS(sorted(lines.items(), reverse=True)))



