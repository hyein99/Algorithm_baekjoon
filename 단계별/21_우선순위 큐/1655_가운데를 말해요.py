import sys
import heapq

N = int(sys.stdin.readline())
maxhp, minhp = [], []    # 최대힙, 최소힙으로 분류
# 최대힙: 중간값보다 작거나 같은 값 들어감
# 최소힙: 중간값보다 큰 값 들어감
for _ in range(N):
    x = int(sys.stdin.readline())
    if len(maxhp) == len(minhp):
        heapq.heappush(maxhp, (-x, x))
    else:
        heapq.heappush(minhp, (x, x))
    if maxhp and minhp and maxhp[0][1] > minhp[0][1]:
        maxx = heapq.heappop(maxhp)[1]
        minx = heapq.heappop(minhp)[1]
        heapq.heappush(maxhp, (-minx, minx))
        heapq.heappush(minhp, (maxx, maxx))
    print(maxhp[0][1])
