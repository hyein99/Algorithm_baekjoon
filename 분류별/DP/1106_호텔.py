# input
C, N = map(int, input().split())
cities = []
for _ in range(N):
    cities.append(list(map(int, input().split())))

dp = [int(1e7) for _ in range(C+100)]  # i명일 때 최소 비용(도시당 비용 최대 100)
dp[0] = 0

for cost, customers in cities:
    for i in range(customers, C+100):  # 해당 도시에서 추가되는 고객 수부터
        dp[i] = min(dp[i-customers] + cost, dp[i])

print(min(dp[C:]))  # C이상 인원 중 최소