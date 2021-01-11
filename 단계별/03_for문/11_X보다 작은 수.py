import sys

a, b = map(int, sys.stdin.readline().rstrip().split())

x = map(int, sys.stdin.readline().rstrip().split())

for j in x:
    if j < b:
        print(j, end=' ')