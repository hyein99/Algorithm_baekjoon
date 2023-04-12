def sub_sum(idx, sub):
    global answer
    if idx >= N:
        return

    for i in range(idx, N):
        if sub+arr[i] == S:
            answer += 1
        sub_sum(i+1, sub+arr[i])

# 입력
N, S = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0
sub_sum(0, 0)
print(answer)