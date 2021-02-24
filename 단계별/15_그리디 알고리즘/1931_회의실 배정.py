import sys

N = int(sys.stdin.readline())
conf = []
for _ in range(N):
    conf.append(list(map(int, sys.stdin.readline().split())))
print(sorted(conf))