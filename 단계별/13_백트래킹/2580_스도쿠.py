import sys
# from collections import deque

def get_sdoku(i, j):
    nlist = list(range(1,10))
    # 가로
    for w in range(9):
        n = sdoku[i][w]
        if n in nlist:
            nlist.remove(n)
            # print(f'가로 {n} 제거')
    # 세로
    for h in range(9):
        n = sdoku[h][j]
        if n in nlist:
            nlist.remove(n)
            # print(f'세로 {n} 제거')
    # 박스
    for b1 in range(3):
        for b2 in range(3):
            n = sdoku[b1+(i//3)*3][b2+(j//3)*3]
            if n in nlist:
                nlist.remove(n)
                # print(f'박스 {n} 제거')
    print(nlist)
    sdoku[i][j] = nlist[0]
    # 숫자 채우기
    # if len(nlist)==1:
    #     sdoku[i][j] = nlist[0]
    #     print(f'숫자채움 > sdoku({i},{j}): {nlist}')
    # else:
    #     print(f'sdoku({i},{j}): {nlist}')


# 스도쿠 받아오기
sdoku = []
for i in range(9):
    sdoku.append(list(map(int, sys.stdin.readline().split())))
# print(sdoku)

for i in range(9):
    for j in range(9):
        if sdoku[i][j] == 0:
            print(i, j)
            get_sdoku(i, j)




# 출력
for sd in sdoku:
    print(*sd, sep=' ')