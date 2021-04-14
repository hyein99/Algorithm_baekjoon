import sys
sys.setrecursionlimit(10000)

# dfs: 재귀
def count_warms(i, j):
    if i<0 or i>=len(ground) or j<0 or j>=len(ground[i]) or ground[i][j]!=1:
        return
    ground[i][j] = '#'

    for d in dir:
        count_warms(i+d[0], j+d[1])
    # count_warms(i-1, j)
    # count_warms(i+1, j)
    # count_warms(i, j-1)
    # count_warms(i, j+1)


T = int(sys.stdin.readline())
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    ground = [[0 for i in range(M)] for j in range(N)]
    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        ground[y][x] = 1

    cnt = 0
    for i in range(len(ground)):
        for j in range(len(ground[i])):
            if ground[i][j] == 1:
                count_warms(i, j)
                cnt += 1
    print(cnt)