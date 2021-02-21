import sys

def LIS(arr):
    result = 1
    dp = [[1, 1] for _ in range(len(arr))]
    # dp[i]: (증가추세일때 arr[i]를 마지막 원소로 가지는 부분수열의 길이, 감소추세일때)
    for i in range(len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:  # 증가 추세
                dp[i][0] = max(dp[i][0], dp[j][0]+1)
            elif arr[i] < arr[j]: # 감소추세
                dp[i][1] = max(dp[i][1], dp[j][1] + 1, dp[j][0] + 1) # 감소추세 or 증가+감소

            if max(dp[i]) > result:
                result = max(dp[i])
    return result

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

print(LIS(arr))
