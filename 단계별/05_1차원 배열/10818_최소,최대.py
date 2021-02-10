import sys

# n = map(int, sys.stdin.readline().rstrip())
n = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().rstrip().split()))

print(min(x), max(x))