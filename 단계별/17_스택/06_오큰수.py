import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

st = []
result = [-1]*N
for i in range(N):
    # print(i, st)
    try:
        while arr[st[-1]] < arr[i]:
            result[st.pop()] = arr[i]
    except:
        pass
    st.append(i)

print(*result, end = ' ')


# while arr:
#     n = arr.pop(0)
#     nge = -1
#     for i in arr:
#         if i > n:
#             nge = i
#             break
#     print(nge, end=' ')