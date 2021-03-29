import sys
from collections import defaultdict
from collections import deque

def dfs():
    pass


def bfs(start):
    max_diameter = 0
    qu = deque()
    qu.append(([start], 0))
    while qu:
        done, length = qu.popleft()
        node = done[-1]
        max_diameter = max(max_diameter, length)
        # print(max_diameter, done)
        for tmp in tree[node]:
            new_node = tmp[0]
            new_length = tmp[1]
            if new_node not in done:
                new_done = done.copy()
                new_done.append(new_node)
                qu.append((new_done, length+new_length))
    return max_diameter


# 입력
V = int(sys.stdin.readline())
tree = defaultdict(list)
for _ in range(V):
    varr = list(map(int, sys.stdin.readline().split()))
    num = varr[0]
    for i in range(1, len(varr)-1, 2):
        if varr[i]>num:
            tree[num].append((varr[i], varr[i+1]))
            tree[varr[i]].append((num, varr[i+1]))

# 지름찾기
max_diameter = 0
for num in tree:
    # print(f'num: {num}')
    max_diameter = max(max_diameter, bfs(num))
print(max_diameter)