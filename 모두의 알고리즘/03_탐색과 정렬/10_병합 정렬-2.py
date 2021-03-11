# Version.2: 일반적인 병합 정렬 알고리즘

def merge_sort(a):
    n = len(a)
    if n <= 1:   # 정렬할 리스트가 한 개 이하면 정렬할 필요 없음
        return
    mid = n // 2
    g1 = a[:mid]
    g2 = a[mid:]
    merge_sort(g1)
    merge_sort(g2)
    print(f'g1: {g1}, g2: {g2}')

    # 두 그룹을 하나로 병합
    i1 = 0
    i2 = 0
    ia = 0
    while i1 < len(g1) and i2 < len(g2):
        if g1[i1] < g2[i2]:
            a[ia] = g1[i1]
            ia += 1
            i1 += 1
        else:
            a[ia] = g2[i2]
            ia += 1
            i2 += 1
    print(f'a: {a}, i1: {i1}, i2: {i2}')
    while i1 < len(g1):
        a[ia] = g1[i1]
        ia += 1
        i1 += 1
    while i2 < len(g2):
        a[ia] = g2[i2]
        ia += 1
        i2 += 1
    print(f'a: {a}')

d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
merge_sort(d)
print(d)

## 알고리즘 분석
# 분할 정복
# 계산 복잡도: O(nlogn) < O(n^2)