from collections import defaultdict

def draw_curve(x, y, d, g):
    graph[(x, y)] = 1
    curve_d = []
    # step 1) 0세대
    end_x, end_y = x + dir[d][0], y + dir[d][1]
    graph[(end_x, end_y)] = 1
    curve_d.append(d)
    # step 2) g만큼 curve 그리기
    for _ in range(g):
        # step 3) 끝점에서 curve 연결
        l = len(curve_d)
        for i in range(l - 1, -1, -1):
            nd = (curve_d[i] + 1) % 4
            end_x, end_y = end_x + dir[nd][0], end_y + dir[nd][1]
            graph[(end_x, end_y)] = 1
            curve_d.append(nd)


# input
N = int(input())
dir = [(1, 0), (0, -1), (-1, 0), (0, 1)]
graph = defaultdict(int)
for _ in range(N):
    x, y, d, g = map(int, input().split())
    draw_curve(x, y, d, g)

# 정사각형 세기
cnt = 0
for i in range(100):
    for j in range(100):
       if graph[(i, j)] and graph[(i+1, j)] and graph[(i, j+1)] and graph[(i+1, j+1)]:
           cnt += 1
print(cnt)