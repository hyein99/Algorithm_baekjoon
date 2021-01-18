# 시간 복잡도 O(N^2)로 풀기
# 버블정렬, 선택정렬, 삽입정렬

# N = int(input())
#
# nlist = []
# for i in range(N):
#     nlist.append(int(input()))
# nlist.sort()
# print(*nlist, sep='\n')

### 선택 정렬 알고리즘 ================================
def sel_sort(a):
    n = len(a)
    for i in range(0, n-1):
        min_idx = i
        for j in range(i+1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]

N = int(input())
nlist = []
for i in range(N):
    nlist.append(int(input()))
sel_sort(nlist)
print(*nlist, sep='\n')