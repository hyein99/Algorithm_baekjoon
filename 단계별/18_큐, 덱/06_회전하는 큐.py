import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
ndq = deque(list(map(int, sys.stdin.readline().split())))
rot = deque([i+1 for i in range(N)])

cnt = 0
while ndq:
    n = ndq[0]
    rrot = rot.copy()
    lrot = rot.copy()
    while True:
        if rrot[0] == n:
            rot = rrot
            break
        elif lrot[0] == n:
            rot = lrot
            break
        rrot.rotate(1)
        lrot.rotate(-1)
        cnt += 1
    rot.popleft()
    ndq.popleft()

print(cnt)