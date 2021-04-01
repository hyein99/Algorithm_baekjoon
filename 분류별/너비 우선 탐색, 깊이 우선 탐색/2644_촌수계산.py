import sys
from collections import defaultdict
from collections import deque

def bfs(a, b):
    done = set()
    done.add(a)
    cnt = 0
    qu = deque()
    qu.append((a, cnt))


    while qu:
        p, cnt = qu.popleft()
        if p == b:
            return cnt
        for c in chon[p]:
            if c not in done:
                done.add(c)
                qu.append((c, cnt+1))
    return -1


# 입력
n = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
chon = defaultdict(list)
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    chon[x].append(y)
    chon[y].append(x)

print(bfs(a, b))
