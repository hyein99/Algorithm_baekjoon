import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque([i+1 for i in range(N)])

final = N
while queue:
    x = queue.popleft()
    if len(queue)==1:
        final = queue.popleft()
    elif not queue:
        final = x
    else:
        queue.append(queue.popleft())
print(final)