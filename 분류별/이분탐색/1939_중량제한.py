from collections import deque
INF = int(1e9)


def bfs(weight):
    qu = deque()
    qu.append((v1, INF))
    visited = [0 for _ in range(N+1)]
    visited[v1] = 1
    while qu:
        n, w = qu.popleft()
        for (b, c) in graph[n]:
            if c < weight:
                continue
            if b == v2:
                return True

            if not visited[b]:
                visited[b] = 1
                qu.append((b, min(w, c)))
    return False


# 입력
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())

result = 0
start, end = 1, INF
while start <= end:
    mid = (start + end) // 2
    if bfs(mid):  # 중량 커버 가능
        result = mid
        start = mid + 1
    else:
        end = mid - 1
print(result)

# 3 4
# 1 2 3
# 1 2 4
# 3 1 2
# 2 3 4
# 1 3