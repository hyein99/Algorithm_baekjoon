import sys
from collections import deque

N = int(sys.stdin.readline())
nlist = deque()
for _ in range(N):
    orders = sys.stdin.readline().split()
    ord = orders[0]
    # print(order)
    if ord == 'push_front':
        nlist.appendleft(int(orders[1]))
    elif ord == 'push_back':
        nlist.append(int(orders[1]))
    elif ord == 'pop_front':
        print(nlist.popleft()) if nlist else print(-1)
    elif ord == 'pop_back':
        print(nlist.pop()) if nlist else print(-1)
    elif ord == 'size':
        print(len(nlist))
    elif ord == 'empty':
        print(0) if nlist else print(1)
    elif ord == 'front':
        print(nlist[0]) if nlist else print(-1)
    else:
        print(nlist[-1]) if nlist else print(-1)
