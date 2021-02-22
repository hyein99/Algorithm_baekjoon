# LCS(Longest Common Subsequence)를 구하는 문제

import sys

def LCS(str1, str2):
    result = 0
    dp = [(0,0) for _ in range(len(str1))]
    # dp[i]: (str1[i]를 마지막으로 하는 문자열 중 str2에 있고 가장 긴 문자열의 길이,
    #         그 문자열의 str2 위치+1)

    for i in range(len(str1)):
        for j in range(i,-1,-1):
            x = str2[dp[j][1]:].find(str1[i])
            if x != -1 and dp[j][0]+1 > dp[i][0]:
                dp[i] = (dp[j][0]+1, dp[j][1]+x+1)
            if dp[i][0] > result:
                result = dp[i][0]
    #         print(dp)
    # print()
    print(dp)
    return result

# 입력
str1 = sys.stdin.readline().rstrip()
str2 = sys.stdin.readline().rstrip()

print(LCS(str1, str2))

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


# A
# - A: A > (1,1) >> dp[0]
# C
# - AC: AC > (2,3) >> dp[1]
# - C: C > (1,0)
# A
# - AA: AA > (2,4)
# - ACA: ACA > (3,4) >> dp[2]
# - CA: CA > ()
# Y
# - AY: x > (0,0) >> dp[3]
# - ACY: x
# - AAY: x
# - ACAY: x
# K
# - AK: AK > (2,5)
# - ACK: ACK > (3,5)
# - AAK: AAK > (3,5)
# - ACAK: ACAK > (4,5) >> dp[4]
# P
# - AP: AP > (2,2)
# - ACP: