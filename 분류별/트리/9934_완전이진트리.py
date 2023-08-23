# https://www.acmicpc.net/problem/9934

from collections import defaultdict, deque

def split_tree(subtree):
    if len(subtree) == 1:
        return subtree[0]

    root = subtree[len(subtree) // 2]
    left = split_tree(subtree[:len(subtree)//2])
    right = split_tree(subtree[len(subtree)//2 + 1:])

    tree[root]['l'] = left
    tree[root]['r'] = right

    return root


# input
K = int(input())
arr = list(map(int, input().split()))
tree = defaultdict(lambda: {})

# step 1) tree 만들기
R = split_tree(arr)

# step 2) tree 출력하기
qu = deque([R])
for _ in range(K):
    stage = []
    next_qu = deque()
    while qu:
        n = qu.popleft()
        stage.append(n)
        if n in tree:
            next_qu.append(tree[n]['l'])
            next_qu.append(tree[n]['r'])
    print(*stage)
    qu = next_qu