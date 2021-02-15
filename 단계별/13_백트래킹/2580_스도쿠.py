import sys

# (i, j) 위치에 가능한 숫자 리턴
def available(i, j):
    nlist = [1,2,3,4,5,6,7,8,9]
    # 가로+세로
    for w in range(9):
        if sdoku[i][w] in nlist:
            nlist.remove(sdoku[i][w])
        if sdoku[w][j] in nlist:
            nlist.remove(sdoku[w][j])
    # 박스
    i //= 3
    j //= 3
    for b1 in range(3):
        for b2 in range(3):
            x = sdoku[b1+i*3][b2+j*3]
            if x in nlist:
                nlist.remove(x)
    return nlist


def DFS(idx):
    global flag
    if flag: # 이미 결과가 나왔을 때(없으면 여러개 출력됨)
        return

    # 종료조건 + 스도쿠 출력
    if idx == len(blank):
        for sd in sdoku:
            print(*sd, sep=' ')
        flag = True
        return

    (i, j) = blank[idx]
    nlist = available(i, j) # 빈칸에 가능한 숫자
    for n in nlist:
        sdoku[i][j] = n
        DFS(idx+1)
        sdoku[i][j] = 0


# 스도쿠 받아오기
sdoku = []
for _ in range(9):
    sdoku.append(list(map(int, sys.stdin.readline().split())))

# 채워야 할 곳 받아오기
blank = []
for i in range(9):
    for j in range(9):
        if sdoku[i][j] == 0:
            blank.append((i, j))

flag = False
DFS(0)
