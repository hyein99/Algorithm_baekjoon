import sys

## case 1
try:
    while True:
        a, b = map(int, sys.stdin.readline().rstrip().split())
        print(a+b)
except:
    exit()

## case 2
# for line in sys.stdin:
#     print(sum(map(int, line.split())))