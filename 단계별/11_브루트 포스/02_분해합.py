N = int(input())

ans=0
for i in range(N):
    num = i + sum(list(map(int, list(str(i)))))
    if num == N:
        ans = i
        break
print(ans)

# 최소값 정하기
# len(str(N))*9 <= i <= N