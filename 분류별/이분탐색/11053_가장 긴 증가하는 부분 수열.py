# 입력
N = int(input())
arr = list(map(int, input().split()))

length = [1 for _ in range(N)]
for i in range(1, N):
    for j in range(i, -1, -1):
        if arr[j] < arr[i]:
            length[i] = max(length[i], length[j] + 1)
print(max(length))