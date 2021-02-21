import sys

# def LIS(arr):
#     dp = defaultdict()
#     dp[arr[0]] = [arr[0], 1] # (마지막 arr숫자, arr길이)
#     # minst = arr[0]   # 최소 start 숫자
#     result = 1       # arr 길이 최대값
#
#     for i in range(1, len(arr)):
#         dp[arr[i]] = [arr[i], 1]
#
#         for n in dp:
#             if dp[n][0] < arr[i]: # arr가 증가추세일 때
#                 dp[n][0] = arr[i]
#                 dp[n][1] += 1
#             if dp[n][1] > result: # arr 길이 최대값 바뀔지
#                 result = dp[n][1]
#     print(dp)
#     return result

def LIS(arr):
    result = 1
    dp = [1 for _ in range(len(arr))]
    # dp[i]: arr[i]를 마지막 원소로 가지는 부분수열의 길이
    for i in range(len(arr)):
        for j in range(i):
            if arr[i] > arr[j] and dp[i] < dp[j]+1: # 증가추세 and 가장 긴 부분수열
                dp[i] = dp[j]+1
                if dp[i]>result:
                    result = dp[i]
    return result

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

print(LIS(arr))