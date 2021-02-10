import sys

# n = int(input())
n = int(sys.stdin.readline())
for i in range(n):
    a, b = sys.stdin.readline().rstrip().split()
    print(int(a)+int(b))