import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

alk, acd  = 0, len(arr)-1
mix = sys.maxsize
result = []
while alk < acd:
    asum = arr[alk]+arr[acd]
    if abs(asum) < abs(mix):
        mix = asum
        result = [arr[alk], arr[acd]]

    if asum < 0:
        alk += 1
    elif asum > 0:
        acd -= 1
    else:
        break
print(*result, sep=' ')