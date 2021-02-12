import sys

def nqueen():

    # queen = 0
    # while queen<N:
    #     chess = [[0] * N for _ in range(N)]
    #     for i in range(N):
    #         for j in range(N):
    #             chess[i][j] = 'q'

    return True


N = int(sys.stdin.readline())
dir = [(0,1), (0,-1), (1,0), (-1,0)]
cnt = 0
for i in range(N):
    for j in range(N):
        nqueen(i, j)
