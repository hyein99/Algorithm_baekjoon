import sys

# 입력
N = int(sys.stdin.readline())
conf = []
for _ in range(N):
    conf.append(list(map(int, sys.stdin.readline().split())))
conf.sort()

cnt, end = 0, 0 # 회의 개수, 끝나는 시간
for i in range(len(conf)):
    if conf[i][0] >= end: # 끝나는 시간 이후 시작 되는 회의
        cnt += 1
        end = conf[i][1]
    if conf[i][1] < end:  # 끝나는 시간이 짧은 회의로 배정
        end = conf[i][1]
print(cnt)