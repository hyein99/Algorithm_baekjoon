import sys

def seperate_paper(paper, w, b):
    sep = 0
    lenp = len(paper)
    for i in range(lenp):
        sep += sum(paper[i])
    if sep==0:
        return w+1, b
    elif sep==lenp*lenp:
        return w, b+1
    else:
        seplist = [
            [row[:lenp//2] for row in paper[:lenp//2]],
            [row[:lenp//2] for row in paper[lenp//2:]],
            [row[lenp//2:] for row in paper[:lenp//2]],
            [row[lenp//2:] for row in paper[lenp//2:]]
        ]
        for slist in seplist:
            w, b = seperate_paper(slist, w, b)
        return w, b


N = int(sys.stdin.readline())
paper = []
for _ in range(N):
    paper.append(list(map(int, sys.stdin.readline().split())))

w, b = seperate_paper(paper, 0, 0)
print(w)
print(b)