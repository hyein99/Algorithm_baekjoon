### Version.2: 일반적인 퀵 정렬 알고리즘
def quick_sort_sub(a, start, end):
    if end-start <= 0:
        return

    pivot = a[end]
    i = start
    for j in range(start, end):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[end] = a[end], a[i]

    # 재귀호출부분
    quick_sort_sub(a, start, i-1) # 기준값보다 작은 그룹을 재귀 호출로 다시 정렬
    quick_sort_sub(a, i+1, end)   # 기준값보다 큰 그룹을 재귀 호출로 다시 정렬


def quick_sort(a):
    quick_sort_sub(a, 0, len(a)-1)

d  = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
quick_sort(d)
print(d)


### 알고리즘 분석
# 시간 복잡도: O(nlogn) (최악의 경우는 O(n^2)이 될수 있음)