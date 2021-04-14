import sys

def quad_tree(qtree):
    sep = 0
    lenp = len(qtree)
    for i in range(lenp):
        sep += sum(qtree[i])
    if sep == 0:
        return '0'
    elif sep == lenp * lenp:
        return '1'
    else:
        seplist = [
            [row[:lenp // 2] for row in qtree[:lenp // 2]],
            [row[lenp // 2:] for row in qtree[:lenp // 2]],
            [row[:lenp // 2] for row in qtree[lenp // 2:]],
            [row[lenp // 2:] for row in qtree[lenp // 2:]]
        ]
        qstr = '('
        for slist in seplist:
            qstr += quad_tree(slist)
        return qstr+')'

N = int(sys.stdin.readline())
qtree = []
for _ in range(N):
    qtree.append(list(map(int, list(sys.stdin.readline().rstrip()))))

print(quad_tree(qtree))