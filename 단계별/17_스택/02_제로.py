import sys

N = int(sys.stdin.readline())

nlist = []
for _ in range(N):
    n = int(sys.stdin.readline())
    if n == 0:
        nlist.pop()
    else:
        nlist.append(n)

print(sum(nlist))