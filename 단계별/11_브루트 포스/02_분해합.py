N = int(input())

ans=0
for i in range(N):
    num = i + sum(list(map(int, list(str(i)))))
    if num == N:
        ans = i
        break
print(ans)
