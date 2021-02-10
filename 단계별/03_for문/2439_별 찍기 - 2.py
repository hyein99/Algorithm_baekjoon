import sys

# n = int(input())
n = int(sys.stdin.readline())
for i in range(1, n+1):
    print(' '*(n-i)+'*'*i)