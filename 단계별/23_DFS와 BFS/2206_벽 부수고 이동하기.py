import sys
from collections import deque

# version 3
def solve_maze():
    qu = deque()
    qu.append((0,0,0,1)) # (행, 열, 벽깨기 수, move)

    while qu:
        x,y,cnt,move = qu.popleft()
        # print(v)
        if x==N-1 and y==M-1:
            return move

        for d in dir: # 다음에 움질일 방향
            nx, ny = x+d[0], y+d[1]
            if 0<=nx<N and 0<=ny<M:                  # 지도 내에 있는지
                if dis[cnt][nx][ny]==0:              # 지나갔는지
                    if maze[nx][ny]=='0':            # 벽이 아님
                        dis[cnt][nx][ny] = 1
                        qu.append((nx, ny, cnt, move+1))
                    elif maze[nx][ny]=='1' and cnt==0:   # 벽인데 벽 뚫은 적 없음
                        dis[cnt][nx][ny] = 1
                        qu.append((nx, ny, cnt+1, move+1))

    return -1


N, M = map(int, sys.stdin.readline().split())
dis = [[[0]*M for _ in range(N)] for _ in range(2)] # 벽 뚫기/안뚫기 버전 구분(방문여부만 확인)

maze = []
dir = [(1,0), (-1,0), (0,1), (0,-1)]     # 동서남북
for _ in range(N):
    maze.append(list(sys.stdin.readline().rstrip()))
print(solve_maze())

# version 2
# queue에 남은 벽깨기 수를 넘겨줌
# 벽 깬 애가 먼저 도착하면 dis[i][j]가 1이상이 되어 넘어감
# >> 지나친 곳도 다시 지나가도록 해줬더니 메모리초과
# def solve_maze():
#     cnt = 1 # 벽깨기
#     qu = deque()
#     qu.append((0,0,cnt)) # (행, 열, 남은벽깨기)
#
#     while qu:
#         v = qu.popleft()
#         # print(v)
#         if v[0]==N-1 and v[1]==M-1:
#             return dis[v[0]][v[1]]
#         for d in dir:
#             i = v[0]+d[0]
#             j = v[1]+d[1]
#             if 0<=i<N and 0<=j<M: #and dis[i][j]==1: # 가능한 경로
#                 if maze[i][j]=='0':                # 정상적인 길
#                     cnt = v[2]
#                 elif maze[i][j]=='1' and v[2]==1:  # 벽 뚫기
#                     cnt = 0
#                 else:
#                     continue
#                 qu.append((i, j, cnt))
#                 dis[i][j] = dis[v[0]][v[1]] + 1
#
#     return -1
#
#
# N, M = map(int, sys.stdin.readline().split())
# dis  = [[1]*M for _ in range(N)]
#
# maze = []
# dir = [(1,0), (-1,0), (0,1), (0,-1)]     # 동서남북
# for _ in range(N):
#     maze.append(list(sys.stdin.readline().rstrip()))
# print(solve_maze())


# version 1
# 벽 깨기를 따로 배열에 넣어준 경우
# 어떤 경로로 왔는지에 따라 벽을 깬 여부를 판단할 수 없음
# def solve_maze_2():
#     qu = deque()
#     qu.append((0,0))
#
#     while qu:
#         v = qu.popleft()
#         # print(v)
#         if v == (N-1, M-1):
#             return dis[v[0]][v[1]]
#         for d in dir:
#             i = v[0]+d[0]
#             j = v[1]+d[1]
#             if 0<=i<N and 0<=j<M and dis[i][j]==1:
#                 # if문 깔끔하게 정리할수 없나?????
#                 if maze[i][j]=='0': # 정상적인 길
#                     qu.append((i,j))
#                     dis[i][j] = dis[v[0]][v[1]] + 1
#                 elif maze[i][j]=='1' and wall[v[0]][v[1]]: # 벽 뚫기
#                     qu.append((i,j))
#                     dis[i][j] = dis[v[0]][v[1]] + 1
#                     wall[i][j] = False
#                 if not wall[v[0]][v[1]]:
#                     wall[i][j] = False
#                 elif wall[v[0]][v[1]]:
#                     wall[i][j] = True
#     return -1
#
# N, M = map(int, sys.stdin.readline().split())
#
# # dis = [[[1, True]]*M for _ in range(N)]  # (거리, 벽깨기) >>> 한번에 바뀜 how????
# dis  = [[1]*M for _ in range(N)]
# wall = [[True]*M for _ in range(N)]
#
# maze = []
# dir = [(1,0), (-1,0), (0,1), (0,-1)]     # 동서남북
# for _ in range(N):
#     maze.append(list(sys.stdin.readline().rstrip()))
# print(solve_maze_2())
