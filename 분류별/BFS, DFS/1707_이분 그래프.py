from collections import defaultdict, deque
import sys
input = sys.stdin.readline

def DFS(u):
    qu = deque([u])
    while qu:
        node = qu.popleft()
        for next_node in graph[node]:
            if next_node in done:
                if done[next_node] == done[node]:
                    return False
            else:
                done[next_node] = -done[node]
                qu.append(next_node)
    return True


# input
K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    done = dict()
    result = True
    for i in range(1, V+1):
        if i not in done:
            done[i] = 1
            if not DFS(i):
                result = False
                break
    if result:
        print("YES")
    else:
        print("NO")