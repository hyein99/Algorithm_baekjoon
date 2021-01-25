import sys
from collections import deque

N = int(sys.stdin.readline())

queue = deque()
for _ in range(N):
    orders = sys.stdin.readline().split()
    order = orders[0]
    if order == 'push':
        queue.append(int(orders[1]))
    elif order == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif order == 'size':
        print(len(queue))
    elif order == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif order == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    else:
        if queue:
            print(queue[-1])
        else:
            print(-1)