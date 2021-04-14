import sys
import heapq

N = int(sys.stdin.readline())
hp = []
for _ in range(N):
    n = int(sys.stdin.readline())
    if n == 0:
        x = heapq.heappop(hp)[1] if hp else 0
        print(x)
    else:
        heapq.heappush(hp, (-n, n))