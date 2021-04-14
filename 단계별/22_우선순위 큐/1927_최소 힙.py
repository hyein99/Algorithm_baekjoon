import sys
import heapq

N = int(sys.stdin.readline())
hp = []
for _ in range(N):
    x = int(sys.stdin.readline())
    print(hp)
    if x == 0:
        n = heapq.heappop(hp)[1] if hp else 0
        print(n)
    else:
        heapq.heappush(hp, (x, x))