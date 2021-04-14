# LCS(Longest Common Subsequence)를 구하는 문제
# solution: 2차원 배열 arr[i][j] str1[i]와 str2[i]를 추가했을 때 최대 길이

import sys

def LCS(str1, str2):
    result = 0
    dp = [0 for _ in range(len(str2))]
    # dp[i]: str2[i]를 마지막으로 하는 str1과 중복되는 부분 수열의 길이

    for i in range(len(str1)):
        for j in range(len(str2)-1, -1, -1): # 이미 추가된 거에 다시 추가하지 않도록
            if str1[i] == str2[j]:           # str1[i]가 str2에 있으면 최소 길이 1
                if dp[j] == 0:
                    dp[j] = 1
                for k in range(j-1, -1, -1):
                    if dp[j] < dp[k]+1:      # 이전에 있는 최대값 + 1
                        dp[j] = dp[k]+1
                if dp[j] > result:
                    result = dp[j]
    return result

# 입력
str1 = sys.stdin.readline().rstrip()
str2 = sys.stdin.readline().rstrip()

print(LCS(str1, str2))