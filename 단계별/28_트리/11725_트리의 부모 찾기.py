import sys
from collections import defaultdict
from collections import deque

N = int(sys.stdin.readline())
root = 1
tree = defaultdict(list)
for _ in range(N-1):
    n1, n2 = map(int, sys.stdin.readline().split())
    tree[n1].append(n2)
    tree[n2].append(n1)

pnode_list = [None]*(N+1)
node_qu = deque()
node_qu.append(root)
while node_qu:
    pnode = node_qu.pop()
    for node in tree[pnode]:
        if not pnode_list[node]:
            pnode_list[node] = pnode
            node_qu.append(node)
print(*pnode_list[2:], sep='\n')