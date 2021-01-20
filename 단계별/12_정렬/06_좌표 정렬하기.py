import sys

## 시간 초과
# N = int(sys.stdin.readline())
#
# nlist = []
# for _ in range(N):
#     i=0
#     ip = list(map(int, sys.stdin.readline().split()))
#     for i in range(len(nlist)):
#         if nlist[i][0]>ip[0] or (nlist[i][0]==ip[0] and nlist[i][1]>ip[1]):
#             break
#     nlist.insert(i, ip)
#
# for j in range(len(nlist)):
#     print(*nlist[j], sep=' ', end='\n')


N = int(sys.stdin.readline())

nlist = []
for _ in range(N):
    nlist.append(list(map(int, sys.stdin.readline().split())))
nlist = sorted(nlist)

for j in range(len(nlist)):
    print(*nlist[j], sep=' ', end='\n')
