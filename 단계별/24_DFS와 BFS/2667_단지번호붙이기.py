# 파이썬 알고리즘 인터뷰_32 섬의 개수

import sys

def get_danji(i, j, cnt):
    if i<0 or i>=len(amap) or j<0 or j>=len(amap[i]) or amap[i][j]!=1:
        return cnt
    amap[i][j] = '#'
    cnt += 1

    # 동서남북
    for d in dir:
        cnt = get_danji(i+d[0], j+d[1], cnt)
    # cnt = get_danji(i, j+1, cnt)
    # cnt = get_danji(i, j-1, cnt)
    # cnt = get_danji(i-1, j, cnt)
    # cnt = get_danji(i+1, j, cnt)
    return cnt

# 지도 받아오기
N = int(sys.stdin.readline())
amap = []
for _ in range(N):
    amap.append(list(map(int, sys.stdin.readline().rstrip())))
# print(amap)

dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
cntlist = []
for i in range(len(amap)):
    for j in range(len(amap[i])):
        if amap[i][j] == 1:
            cnt = get_danji(i, j, 0)
            cntlist.append(cnt)

print(len(cntlist))
print(*sorted(cntlist), sep='\n')


