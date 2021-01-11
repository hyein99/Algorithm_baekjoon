import sys

a = int(sys.stdin.readline().rstrip())
b = int(sys.stdin.readline().rstrip())
c = int(sys.stdin.readline().rstrip())
mul = a*b*c

arr = [int(i) for i in str(mul)]
for i in range(10):
    print(arr.count(i))