# LCS(Longest Common Subsequence)를 구하는 문제

import sys

def LCS(str1, str2):
    result = 0
    dp = [[0,0] for _ in range(len(str1))]
    # dp[i]: (str1[i]를 마지막으로 하는 문자열 중 str2에 있고 가장 긴 문자열의 길이,
    #         그 문자열의 str2 위치+1)

    for i in range(len(str1)):
        for j in range(i,-1,-1):
            x = str2[dp[j][1]:].find(str1[i])
            if x != -1 and (                  # str[i]가 str2에 존재
                    dp[j][0]+1 > dp[i][0] or  # 가장 긴 문자열
                    (dp[j][0]+1 == dp[i][0] and dp[i][1] > dp[j][1]+x+1)):
                     # 길이가 같고 끝난 str2위치가 더 짧은 경우
                dp[i] = (dp[j][0]+1, dp[j][1]+x+1)
            if dp[i][0] > result:
                result = dp[i][0]
    print(dp)
    return result

# 입력
str1 = sys.stdin.readline().rstrip()
str2 = sys.stdin.readline().rstrip()

print(LCS(str1, str2))

# abcdef
# cdefabc

# SKDFHWEODJKSFSDFJK
# WKJSDHFOWEFKJDVKSDF
# 정답: 10, 이 코드: 9
#
# KJSDFKSDFLKDFJS
# SKDJKFLSKDJFLKSDJF
# 정답: 10, 이 코드: 9
#
# LKSDJFLKJWPOJSDLKJFSDF
# OISJDKFJLKEJFSLKJDIFJSLDK
# 정답: 13, 이 코드: 11
