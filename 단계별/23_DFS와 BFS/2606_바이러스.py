import sys
from collections import defaultdict
from collections import deque


# dfs: 스택(역순방문)
def count_virus_dfs():
    done = []
    st = deque()
    st.append(1)
    while st:
        p = st.pop()
        if p not in done:
            done.append(p)
            for i in virus[p]:
                st.append(i)

    # print(done)
    return len(done)-1

# bfs: 큐
def count_virus_bfs():
    done = [1]
    qu = deque()
    qu.append(1)
    while qu:
        p = qu.popleft()
        for i in virus[p]:
            if i not in done:
                done.append(i)
                qu.append(i)

    # print(done)
    return len(done)-1


# 노드 받아오기
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
virus = defaultdict(list)
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    virus[a].append(b)
    virus[b].append(a)

# print('dfs') # 1 2 3 5 6
print(count_virus_dfs())
# print('bfs') # 1 2 5 3 6
print(count_virus_bfs())
