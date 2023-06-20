from collections import defaultdict

def DFS(x, y, cnt, p):
    global total_prob
    if cnt == T:
        total_prob += p
        return

    for i in range(4):
        nx, ny, np = x + darr[i][0], y + darr[i][1], p * parr[i]
        if not done[(nx, ny)]:  # 단순하지 않은 경로
            done[(nx, ny)] = 1
            DFS(nx, ny, cnt + 1, np)
            done[(nx, ny)] = 0  # 다른 조합으로 된 경로에 영향 미치지 않기 위해


# input
T, E, W, S, N = map(int, input().split())

total_prob = 0
parr = [E/100, W/100, S/100, N/100]
darr = [(0,1), (0,-1), (1,0), (-1,0)]
done = defaultdict(int)
done[(0, 0)] = 1
DFS(0, 0, 0, 1)

# output
print(total_prob)