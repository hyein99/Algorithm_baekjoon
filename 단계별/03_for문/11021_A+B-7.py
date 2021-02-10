import sys

# n = int(input())
n = int(sys.stdin.readline())
for i in range(n):
    a, b = sys.stdin.readline().rstrip().split()
    print('Case #{}: {}'.format(i+1, int(a)+int(b)))