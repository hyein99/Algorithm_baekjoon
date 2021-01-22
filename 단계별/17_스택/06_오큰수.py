import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

# nlist = [-1]*N
# nge = arr[N-1]
# for i in range(N-2, -1, -1):
#     if arr[i] > nge and i > 0:
#         nge = arr[i]
#     if arr[i] < arr[i+1]:
#         nge = arr[i+1]
#     nlist[i] = nge
# print(*nlist, sep=' ')
while arr:
    n = arr.pop(0)
    nge = -1
    for i in arr:
        if i > n:
            nge = i
            break
    print(nge, end=' ')