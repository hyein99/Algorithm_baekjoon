import sys
from collections import defaultdict
from collections import deque

def dfs(start):
    '''
    임의의 x에서 가장 거리가 먼 노트 y를 구하면 y는 반드시 지름을 구성하는 한 노드
    (증명)
    전제: 트리의 지름은 u에서 v까지 거리
    i) 만약 y가 u또는 v면 무조건 참
    ii) y가 u또는 v가 아닐 때
    >> dist(x,y) = dist(x,t)+dist(t,y)인데 dist(t,y)가 dist(t,v)나 dist(t,u)보다 크다는 말임
    >> dist(t,y)가 dist(t,u)나 dist(t,v)보다 크면 트리의 지름이 u-v가 아니라 u-y가 됨.
    >> 따라서 y는 무조건 u,v가 됨
    '''
    visit = [-1] * (V + 1)
    st = deque()
    st.append(start)
    visit[start] = 0
    end, max_diameter = 0, 0

    while st:
        cur_node = st.pop()
        for next_node, length in tree[cur_node]:
            if visit[next_node] == -1:
                visit[next_node] = visit[cur_node] + length
                st.append(next_node)
                if max_diameter < visit[next_node]:
                    max_diameter = visit[next_node]
                    end = next_node

    return end, max_diameter


# BFS(방문한 곳 리스트로 보관)
def bfs1(start):
    max_diameter = 0
    qu = deque()
    qu.append(([start], 0))
    while qu:
        done, length = qu.popleft()
        node = done[-1]
        if length > max_diameter:
            max_diameter = length
            end = node
        # print(max_diameter, done)
        for tmp in tree[node]:
            new_node = tmp[0]
            new_length = tmp[1]
            if new_node not in done:
                new_done = done.copy()
                new_done.append(new_node)
                qu.append((new_done, length+new_length))
    return end, max_diameter

# BFS(방문 표시)
def bfs2(start):
    visit = [-1] * (V + 1)
    qu = deque()
    qu.append(start)
    visit[start] = 0
    end, max_diameter = 0, 0

    while qu:
        cur_node = qu.popleft()
        for next_node, length in tree[cur_node]:
            if visit[next_node] == -1:
                visit[next_node] = visit[cur_node] + length
                qu.append(next_node)
                if max_diameter < visit[next_node]:
                    max_diameter = visit[next_node]
                    end = next_node
    return end, max_diameter


# 입력
V = int(sys.stdin.readline())
tree = defaultdict(list)
for _ in range(V):
    varr = list(map(int, sys.stdin.readline().split()))
    num = varr[0]
    for i in range(1, len(varr)-1, 2):
        tree[num].append((varr[i], varr[i+1]))

# 지름찾기
y, diameter = dfs(1)
tmp, max_diameter = dfs(y)
print(max_diameter)