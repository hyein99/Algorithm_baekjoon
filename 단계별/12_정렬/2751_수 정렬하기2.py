# 시간 복잡도 O(nlogn)으로 풀기
# 병합 정렬, 합 정렬, 기수 정렬, 카운팅 정렬

def merge_sort(nlist):
    l = len(nlist)
    if l <= 1:
        return

    mid = l//2
    g1 = nlist[:mid]
    g2 = nlist[mid:]
    merge_sort(g1)
    merge_sort(g2)

    i1=0; i2=0; idx=0
    while i1 < len(g1) and i2 < len(g2):
        if g1[i1] < g2[i2]:
            nlist[idx] = g1[i1]
            i1 += 1
            idx += 1
        else:
            nlist[idx] = g2[i2]
            i2 += 1
            idx += 1
    while i1 < len(g1):
        nlist[idx] = g1[i1]
        i1 += 1
        idx += 1
    while i2 < len(g2):
        nlist[idx] = g2[i2]
        i2 += 1
        idx += 1

N = int(input())
nlist = []
for i in range(N):
    nlist.append(int(input()))
merge_sort(nlist)
print(*nlist, sep='\n')


## sorted로도 되네,,
# import sys
#
# n = int(sys.stdin.readline())
# nlist = list(map(int, sys.stdin.read().split()))
# print(*sorted(nlist), sep='\n')
