import sys

arr = []
for i in range(9):
    arr.append(int(sys.stdin.readline().rstrip()))
max = max(arr)
print(max)
print(arr.index(max)+1)