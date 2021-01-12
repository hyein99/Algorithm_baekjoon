word = list(input())
clist = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

cnt = 0
for w in word:
    for ci, c in enumerate(clist):
        if w in c:
            cnt += ci+3
print(cnt)