import sys

N = int(sys.stdin.readline())

nlist = []
for _ in range(N):
    [a, b] = list(map(int, sys.stdin.readline().split()))
    nlist.append([b, a])
nlist = sorted(nlist)

for j in range(len(nlist)):
    print(nlist[j][1], nlist[j][0])