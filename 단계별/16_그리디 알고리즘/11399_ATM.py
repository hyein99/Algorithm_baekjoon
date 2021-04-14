import sys

N = int(sys.stdin.readline())
people = sorted(list(map(int, sys.stdin.readline().rstrip().split())))

# 빨리 걸리는 사람부터
sum = 0
for i in range(N):
    sum += people[i]*(N-i) # i번째 사람 소용시간*기다리는 사람 수
print(sum)