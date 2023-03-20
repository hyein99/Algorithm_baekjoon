from collections import defaultdict
import heapq
INF = 1e9

# 입력
n = int(input())
m = int(input())
graph = defaultdict(list)
for _ in range(m):
    x, y, c = map(int, input().split())
    graph[x].append((y, c))
start, end = map(int, input().split())

qu = []
heapq.heappush(qu, (0, start, [start]))  # 비용, 노드, 도시 순서
distance = [INF for _ in range(n+1)]
distance[start] = 0
ans_cities = []
while qu:
    cost, node, cities = heapq.heappop(qu)
    if distance[node] < cost:
        continue

    for (y, c) in graph[node]:
        if cost + c < distance[y]:
            distance[y] = cost + c
            heapq.heappush(qu, (cost+c, y, cities+[y]))

            if y == end:
                ans_cities = cities+[y]


# 출력
print(distance[end])  # 최소 비용
print(len(ans_cities))  # 도시 개수
print(*ans_cities, sep=' ')  # 도시 순서대로