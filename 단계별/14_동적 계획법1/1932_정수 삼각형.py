import sys

def get_trimax(n):
    for i in range(1, n):
        tri[i][0] += tri[i-1][0]   # 양 끝값은 경우의 수 1가지
        tri[i][-1] += tri[i-1][-1]
        for j in range(1, len(tri[i])-1):
            tri[i][j] += max(tri[i-1][j-1], tri[i-1][j])
    return max(tri[n-1])


n = int(sys.stdin.readline())
tri = []
for _ in range(n):
    tri.append(list(map(int, sys.stdin.readline().split())))

print(get_trimax(n))