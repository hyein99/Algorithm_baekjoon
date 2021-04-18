import sys

def find_cnt(n):
    # n보다 작은 자연수의 곱(i*j)의 개수를 구하는 함수
    cnt = 0
    for i in range(1, N+1):
        cnt += min(n//i, N)
    return cnt

N = int(sys.stdin.readline())
k = int(sys.stdin.readline()) # k번째 수 찾기

start, end = 1, k
while start <= end:
    mid = start + (end-start)//2

    if find_cnt(mid) >= k:
        end = mid - 1
    else:
        start = mid + 1

print(start)


# 1 2 3
# 2 4 6
# 3 6 9

# 1 2 3 4
# 2 4 6 8
# 3 6 9 12
# 4 8 12 16