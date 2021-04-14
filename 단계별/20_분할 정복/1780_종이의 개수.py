import sys

# arr를 넘겨주면 재귀할 때마다 copy실행
def seperate_paper(fr1, fr2, lenp):
    global paper, x, y, z
    num = paper[fr1][fr2]
    breakflag = False

    for i in range(fr1, fr1+lenp):
        if breakflag:
            break
        for j in range(fr2, fr2+lenp):
            if paper[i][j] != num:
                n = lenp // 3
                treelist = [
                    [fr1, fr2, n],
                    [fr1, fr2 + n, n],
                    [fr1, fr2 + 2 * n, n],
                    [fr1 + n, fr2, n],
                    [fr1 + n, fr2 + n, n],
                    [fr1 + n, fr2 + 2 * n, n],
                    [fr1 + 2 * n, fr2, n],
                    [fr1 + 2 * n, fr2 + n, n],
                    [fr1 + 2 * n, fr2 + 2 * n, n]
                ]
                for tree in treelist:
                    seperate_paper(*tree)
                breakflag = True
                break

    if not breakflag: # break로 끝났으면 바로 pass
        if num == -1:
            x += 1
        elif num == 0:
            y += 1
        else:
            z += 1



N = int(sys.stdin.readline())
paper = []
for _ in range(N):
    paper.append(list(map(int, sys.stdin.readline().split())))

x,y,z = 0,0,0
seperate_paper(0, 0, N)
print(x)
print(y)
print(z)