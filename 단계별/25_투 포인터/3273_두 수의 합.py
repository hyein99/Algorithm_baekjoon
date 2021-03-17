import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())

l, r = 0, n-1
arr.sort()
cnt = 0
while l < r:
    nsum = arr[l]+ arr[r]
    if nsum > x:
        r -= 1
    elif nsum < x:
        l += 1
    else:
        cnt += 1
        r -= 1
        l += 1
print(cnt)