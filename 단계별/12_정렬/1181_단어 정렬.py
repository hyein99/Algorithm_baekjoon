N = int(input())

wlist = [set() for _ in range(50)]
for _ in range(N):
    w = input()
    wlist[len(w)-1].add(w)

for i in range(len(wlist)):
    if len(wlist[i])==0:
        continue
    print(*sorted(wlist[i]), sep='\n')
