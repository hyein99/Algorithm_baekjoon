# Version.2: 일반적인 삽입 정렬 알고리즘

def ins_sort(r):
    a = len(r)
    for i in range(1, a):
        key = r[i]    # i번째에 있는 값을 key에 저장
        j = i - 1     # j를 i 바로 왼쪽 위치로 저장
        while j >= 0 and r[j] > key:
            r[j+1] = r[j]
            j -= 1
        r[j+1] = key

d = [2, 4, 5, 1, 3]
ins_sort(d)
print(d)

## 알고리즘 분석
# 시간복잡도: O(n^2)