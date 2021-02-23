import sys

N = int(sys.stdin.readline())
people = sorted(list(map(int, sys.stdin.readline().rstrip().split())))

sum = 0
for i in range(N):
    sum += people[i]*(N-i)
print(sum)