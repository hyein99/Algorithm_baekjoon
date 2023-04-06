def binary_search(n):
    start, end = 1, len(ascending_arr)-1
    while start < end:
        mid = (start+end)//2
        if ascending_arr[mid] >= n:
            end = mid
        else:
            start = mid + 1
    return end


# 입력
N = int(input())
arr = list(map(int, input().split()))

ascending_arr = [0]
for a in arr:
    print(ascending_arr)
    if ascending_arr[-1] < a:
        ascending_arr.append(a)
    else:
        ascending_arr[binary_search(a)] = a

print(len(ascending_arr)-1)
print(ascending_arr)
# 6
# 10 20 10 30 20 50 >> 4

# 5
# 10 20 30 16 15 >> 3

# 5
# 10 11 15 14 16 >> 4