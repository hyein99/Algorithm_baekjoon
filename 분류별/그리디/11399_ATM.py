# 입력
N = int(input())
P = list(map(int, input().split()))

P.sort()
answer = 0
cur_time = 0
for i in P:
    cur_time = cur_time + i
    answer += cur_time

# 출력
print(answer)