# 플로이드 알고리즘

# input
n = int(input())
m = int(input())
cities = [[int(1e9)]*n for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    cities[a-1][b-1] = min(cities[a-1][b-1], c)

for i in range(n):
    cities[i][i] = 0
for idx in range(n):
    for i in range(n):
        for j in range(n):  # i > j에서 idx 노드 거쳐 가는 경우
            cities[i][j] = min(cities[i][j], cities[i][idx] + cities[idx][j])

# output
for i in range(n):
    for j in range(n):
        if cities[i][j] >= int(1e9):
            print(0, end=" ")
        else:
            print(cities[i][j], end=" ")
    print()
