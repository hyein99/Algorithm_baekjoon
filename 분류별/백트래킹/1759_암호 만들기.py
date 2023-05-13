def encode(s, i):
    if len(s) == L:
        # 최소 한개 모음 + 최소 두개 자음
        vow = set(s)-set(['a', 'e', 'i', 'o', 'u'])
        if len(vow) >= 2 and L-len(vow) >= 1:
            print(s)
        return

    for idx in range(i, C):
        encode(s+arr[idx], idx+1)


# input
L, C = map(int, input().split())
arr = list(input().split())

arr.sort()
encode('', 0)