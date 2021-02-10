import sys

N = int(sys.stdin.readline())

mlist = [[] for _ in range(200)]
for _ in range(N):
    age, name = sys.stdin.readline().split()
    mlist[int(age)-1].append(name)

for i in range(len(mlist)):
    for j in range(len(mlist[i])):
        print(i+1, mlist[i][j])