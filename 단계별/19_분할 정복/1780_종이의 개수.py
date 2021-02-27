import sys

def seperate_paper(paper, x, y, z):
    lenp = len(paper)
    sep = 0
    zeroflag = True
    for i in range(lenp):
        sep += sum(paper[i])
        if 1 in paper[i] or -1 in paper[i]:
            zeroflag = False
    if sep == -(lenp*lenp):
        return x+1, y, z
    elif sep == 0 and zeroflag:
        return x, y+1, z
    elif sep == lenp*lenp:
        return x, y, z+1

    else:
        tmp = lenp//3
        seplist = [
            [row[:tmp] for row in paper[:tmp]],
            [row[tmp:tmp*2] for row in paper[:tmp]],
            [row[tmp*2:] for row in paper[:tmp]],
            [row[:tmp] for row in paper[tmp:tmp*2]],
            [row[tmp:tmp*2] for row in paper[tmp:tmp*2]],
            [row[tmp*2:] for row in paper[tmp:tmp*2]],
            [row[:tmp] for row in paper[tmp*2:]],
            [row[tmp:tmp*2] for row in paper[tmp*2:]],
            [row[tmp*2:] for row in paper[tmp*2:]]
        ]
        for slist in seplist:
            x,y,z = seperate_paper(slist, x,y,z)
        return x,y,z


N = int(sys.stdin.readline())
paper = []
for _ in range(N):
    paper.append(list(map(int, sys.stdin.readline().split())))

x, y, z = seperate_paper(paper, 0, 0, 0)
print(x)
print(y)
print(z)