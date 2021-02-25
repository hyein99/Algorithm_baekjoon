import sys

N = int(sys.stdin.readline())
conf = []
for _ in range(N):
    conf.append(list(map(int, sys.stdin.readline().split())))
conf.sort()

cnt, end = 0, 0
for i in range(len(conf)):
    print(i)
    if conf[i][0] >= end:
        cnt += 1
        end = conf[i][1]
    if conf[i][1] < end:
        end = conf[i][1]
print(cnt)