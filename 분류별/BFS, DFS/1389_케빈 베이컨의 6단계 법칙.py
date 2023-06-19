import sys
from collections import defaultdict
from collections import deque

def bfs(start):
    cbacon = [-1]*(N+1) # 방문 표시이자 케빈베이컨
    qu = deque()
    qu.append(start)
    cbacon[start] = 0   # 방문 표시

    while qu:
        fr = qu.popleft()
        for next_fr in friends[fr]:
            if cbacon[next_fr] == -1:
                cbacon[next_fr] = cbacon[fr]+1
                qu.append(next_fr)

    return sum(cbacon) + 1 # cbacon[0] 값 제외

# 입력
N, M = map(int, sys.stdin.readline().split())
friends = defaultdict(list)
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    friends[a].append(b)
    friends[b].append(a)

min_cbacon = sys.maxsize
min_user = 1
for i in range(1, N+1):
    current_cbacon = bfs(i)
    if current_cbacon < min_cbacon:
        min_cbacon = current_cbacon
        min_user = i
print(min_user)