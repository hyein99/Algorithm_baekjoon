import sys
from collections import defaultdict
from collections import deque

def dfs(discovered, start):
    st = deque()
    st.append(start)
    while st:
        u = st.pop()
        if u not in discovered:
            discovered.append(u)
            for v in graph[u]:
                st.append(v)
    return discovered


def bfs(discovered, start):
    qu = deque()
    qu.append(start)
    discovered.append(start)
    while qu:
        u = qu.popleft()
        for v in graph[u]:
            if v not in discovered:
                discovered.append(v)
                qu.append(v)
    return discovered

# 입력
N, M = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

discovered = []
cnt = 0
for i in range(1, N+1):
    if i not in discovered:
        discovered=dfs(discovered, i)
        cnt += 1
print(cnt)