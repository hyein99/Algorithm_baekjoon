import sys

N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

asum = arr[0]
l, r = 0, 0
minlen = N+1
while r < len(arr):
    while asum - arr[l] >= S:  # 최소 길이 조정(제일 먼저 해줘야 마지막에 추가된 숫자 기준 자를수 있음)
        asum -= arr[l]
        l += 1

    if asum < S:  # S이상이 될때까지 더하기
        r += 1
        if r<len(arr):
            asum += arr[r]
    else:
        minlen = min(minlen, r-l+1)
        if r+1<len(arr):
            asum = asum - arr[l] + arr[r+1]
        l += 1
        r = r + 1 if l<r+1 else r + 2    # 같을 경우 다음 두칸으로

if minlen == N+1:
    print(0)
else:
    print(minlen)



