import sys
input = sys.stdin.readline
import heapq


def dijkstra(start):
    h = []
    heapq.heappush(h, (0, start))
    tarr = [int(1e9)] * (n+1)
    tarr[start] = 0
    cnt, max_time = 0, 0

    while h:
        cur_t, cur_c = heapq.heappop(h)
        if tarr[cur_c] < cur_t:
            continue

        cnt += 1
        max_time = max(max_time, cur_t)

        for next_c, next_t in graph[cur_c]:
            if tarr[next_c] > tarr[cur_c] + next_t:
                tarr[next_c] = tarr[cur_c] + next_t
                heapq.heappush(h, (tarr[next_c], next_c))

    return cnt, max_time


T = int(input())
for _ in range(T):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))
    print(*dijkstra(c))