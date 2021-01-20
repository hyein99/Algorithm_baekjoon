def binary_search(a, x):
    start = 0
    end = len(a)-1

    while start <= end:
        mid = (start+end)//2
        if x == a[mid]:
            return mid
        elif x > a[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1

d = [1, 4, 9, 16, 25, 36, 49, 64, 81]
print(binary_search(d, 36))
print(binary_search(d, 50))


### 알고리즘 분석
# 계산 복잡도: O(logn) < O(n)