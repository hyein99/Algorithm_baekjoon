# https://www.acmicpc.net/problem/16235


"""
N*N 땅 1*1 크기
(r, c) r, c, >= 1
S2D2: 칸 양분 조사해 전송 > 모든 칸에 대해 조사
초기값: 5만큼씩 들어있음

M개 나무 구매 (한 칸에 여러 나무 심기 가능)
봄: 나이 만큼 양분 먹고 나이 +1(그 칸에 있는 양분만. 나무 여러개면 애기나무부터. 못먹으면 죽음)
여름: 죽은 나무가 양분으로(죽은 나무 나이 //2)
가을: 나무 번식(나이 5의 배수인 나무만. 인접한 8개 칸에 나이 1인 나무. 벗어나면 패스)
겨울: 양분 추가 A[r][c] 만큼씩 추가됨
"""

from collections import defaultdict, deque

# input
N, M, K = map(int, input().split())
food = []
for _ in range(N):
    food.append(list(map(int, input().split())))
ground = [[5 for _ in range(N)] for _ in range(N)]
trees = defaultdict(lambda: deque())
for _ in range(M):
    x, y, z = map(int, input().split())
    trees[(x-1, y-1)].append(z)
for tree in trees:
    trees[tree] = sorted(trees[tree])  # order trees by age
dir = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

tree_cnt = M
for _ in range(K):
    # step 1) spring
    dead_food = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if trees[(i, j)]:
                tree = trees[(i, j)]
                survived = deque()
                for t in tree:  # from younger tree
                    if ground[i][j] >= t:
                        ground[i][j] -= t
                        survived.append(t+1)
                    else:
                        dead_food[i][j] += t//2
                        tree_cnt -= 1
                trees[(i, j)] = survived

    # step 2) fall
    for (x, y) in trees:
        for t in trees[(x, y)]:
            if t%5 == 0:
                for d in dir:
                    nx, ny = x+d[0], y+d[1]
                    if 0<=nx<N and 0<=ny<N:
                        trees[(nx, ny)].appendleft(1)
                        tree_cnt += 1

    # step 3) summer + winter
    for i in range(N):
        for j in range(N):
            ground[i][j] += dead_food[i][j] + food[i][j]

# output
print(tree_cnt)