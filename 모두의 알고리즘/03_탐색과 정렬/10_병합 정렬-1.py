# Version.1: 쉽게 설명한 병합 정렬 알고리즘

def merge_sort(a):
    n = len(a)
    if n <= 1:   # 정렬할 리스트가 한 개 이하면 정렬할 필요 없음
        return a
    mid = n // 2
    g1 = merge_sort(a[:mid])
    g2 = merge_sort(a[mid:])

    # 두 그룹을 하나로 병합
    result = []
    while g1 and g2:
        if g1[0] < g2[0]:
            result.append(g1.pop(0))
        else:
            result.append(g2.pop(0))
    while g1:
        result.append(g1.pop(0))
    while g2:
        result.append(g2.pop(0))
    return result

d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
print(merge_sort(d))