# DFS: 깊이우선탐색
# BFS: 넓이우선탐색

import sys
from collections import deque

# DFS: 스택
def get_dfs(start):
    done = []     # 이미 방문한 곳
    st = deque()  # 앞으로 방문할 곳
    st.append(start)
    while st:
        p = st.pop()
        if p not in done:
            done.append(p)
            # print(p, end=' ')
            if p in route:
                st.extend(sorted(route[p], reverse=True))
    return done


# BFS: 큐
def get_bfs(start):
    done = []      # 이미 방문한 곳
    done.append(start)
    qu = deque()   # 앞으로 방문할 곳
    qu.append(start)
    while qu:
        p = qu.popleft()
        # done.append(p)
        # print(p, end=' ')
        tmp = []
        if p in route:
            for v in route[p]:
                if v not in done:
                    tmp.append(v)
                    # done.append(v)
            qu.extend(sorted(tmp))
            done.extend(sorted(tmp))
    return done

# 그래프 받아오기
N, M, V = map(int, sys.stdin.readline().split())
route = {}   # 그래프 보관할 dic
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    if a in route:
        route[a].add(b)
    else:
        route[a] = {b}
    if b in route:
        route[b].add(a)
    else:
        route[b] = {a}
# print(route)


print(*get_dfs(V), sep=' ')
print(*get_bfs(V), sep=' ')
