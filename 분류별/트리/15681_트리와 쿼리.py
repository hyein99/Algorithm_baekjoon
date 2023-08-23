import sys
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(1000000000)

def countSubtree(currentNode):
    size[currentNode] = 1
    for Node in tree[currentNode]:
        if not size[Node]:
            countSubtree(Node)
            size[currentNode] += size[Node]


# input
N, R, Q = map(int, input().split())
tree = defaultdict(list)
size = [0] * (N+1)
for _ in range(N-1):
    U, V = map(int, input().split())
    tree[U].append(V)
    tree[V].append(U)

countSubtree(R)
for _ in range(Q):
    U = int(input())
    print(size[U])  # 서브 트리에 속한 정점 수
