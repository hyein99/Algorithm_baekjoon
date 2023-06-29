# input
N = int(input())

h = [1]
i = 1
n = 1
dp = [int(1e9) for _ in range(N+1)]
dp[0] = 0
dp[1] = 1
while True:
    n = h[-1] + i*6 - (1+2*(i-1))
    if n > N:
        break
    i += 1
    h.append(n)
    dp[n] = 1

for i in range(1, N+1):
    for j in range(len(h)):
        if i < h[j]:
            break
        dp[i] = min(dp[i], dp[i-h[j]] + 1)
print(dp[N])