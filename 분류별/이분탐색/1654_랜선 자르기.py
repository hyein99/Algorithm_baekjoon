def cut(l):
    cnt = 0
    for a in arr:
        cnt += a//l
    return cnt


def binary_search(target, start, end):
    while start <= end:
        mid = (start + end) // 2
        c = cut(mid)
        if c < target:  # 덜 잘라야 함
            end = mid - 1
        else:
            start = mid + 1

    return end


# 입력
K, N = map(int, input().split())
arr = [int(input()) for _ in range(K)]

result = binary_search(N, 1, max(arr))  # start: 0, end: arr 최대값
print(result)