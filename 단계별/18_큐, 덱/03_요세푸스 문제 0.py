import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
queue = deque([i+1 for i in range(N)])

yose = []
while queue:
    queue.rotate(-(K-1))
    yose.append(str(queue.popleft()))

print('<', ', '.join(yose), '>', sep='')