import sys
from collections import deque

def count_maze(maze, start, end):
    return


# 미로 받아오기
N, M = map(int, sys.stdin.readline().split())
maze = []
for _ in range(N):
    maze.append(list(sys.stdin.readline().rstrip()))
# print(maze)

cnt = count_maze(0, (0,0), (M-1, N-1))
print(cnt)

