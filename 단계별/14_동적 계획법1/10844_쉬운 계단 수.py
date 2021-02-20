# 1) 9(0개, 1개)
  # 1,2,3,4,5,6,7,8,9
# 2) 8+9=17(1개, 1개)
  # 12 ... 89 /(8)
  # 10 ... 98 \(9)
# 3) 7+8+8+9=32(1개, 2개)
  # 123 ... 789 //(7)
  # 121 ... 898 /\(8)
  # 101 ... 989 \/(9)
  # 210 ... 987 \\(8)
# 4) 6+7+7+8+8+8+8+9=61 (3개, 3개)
  # 1234 ... 6789 ///(6)
  # 1232 ... 7898 //\(7)
  # 1212 ... 8989 /\/(8)
  # 1210 ... 8987 /\\(8)
  # 1012 ... 8789 \//(8)
  # 1010 ... 9898 \/\(9)
  # 2101 ... 9878 \\/(8)
  # 3210 ... 9876 \\\(7)
# 5) 5+6+6+7+7+7+7+8+8+8+8+8+8+8+8+9=118
# 5) 61*2-6 = 116 (4개, 6개)
  # 12345 ... 5678 ////


import sys

def count_stairs(N):
    stairs = [1 for _ in range(10)]
    for i in range(1, N):
        tmp = [0 for _ in range(10)]
        tmp[1] += stairs[0]
        tmp[8] += stairs[9]
        for j in range(1, len(stairs)-1):
            tmp[j-1] += stairs[j]
            tmp[j+1] += stairs[j]
        stairs = tmp
    # print(stairs)
    return sum(stairs[1:])%1000000000


# 시간 초과 + 메모리초과
# def count_stairs(N):
#     if N==1:
#         return 9
#     dp = defaultdict(list)
#     dp[1] = [1,2,3,4,5,6,7,8,9]
#     for i in range(2, N+1):
#         dp[i] = [int(str(n)+str(n%10-1)) for n in dp[i-1] if len(str(n)+str(n%10-1))==i]
#         dp[i].extend([int(str(n)+str(n%10+1)) for n in dp[i-1] if len(str(n)+str(n%10+1))==i])
#     return len(dp[N])

N = int(sys.stdin.readline())
print(count_stairs(N))
