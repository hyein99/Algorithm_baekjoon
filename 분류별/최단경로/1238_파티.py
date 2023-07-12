import sys
input = sys.stdin.readline
import heapq

def dijkstra(start):
    h = []
    heapq.heappush(h, (0, start))
    distances = [int(1e9)] * (N+1)
    distances[start] = 0

    while h:
        d, n = heapq.heappop(h)
        if distances[n] < d:
            continue

        for next_n, next_d in roads[n]:
            if distances[next_n] > d + next_d:
                distances[next_n] = d + next_d
                heapq.heappush(h, (distances[next_n], next_n))

    return distances


# input
N, M, X = map(int, input().split())
roads = [[] for _ in range(N+1)]
for _ in range(M):
    start, end, t = map(int, input().split())
    roads[start].append((end, t))

distances_arr = []
for i in range(N+1):
    distances_arr.append(dijkstra(i))

print(max([distances_arr[i][X] + distances_arr[X][i] for i in range(1, N+1)]))