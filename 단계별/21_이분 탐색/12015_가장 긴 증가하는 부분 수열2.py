import sys
import bisect

# 풀이 2) bisect
# 입력
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

ascending_arr = [0]
for a in arr:
    if ascending_arr[-1] < a:
        # 마지막으로 추가한 숫자보다 클 경우 증가하는 수열에 추가
        ascending_arr.append(a)  
    else:
        # 마지막으로 추가한 숫자보다 작을 경우 들어갈 자리를 찾음
        # 그 자리를 a로 교체(더 작은 숫자가 들어가게 됨)
        ascending_arr[bisect.bisect_left(ascending_arr, a)] = a

print(len(ascending_arr)-1) # 0제외


# 풀이 1) 이분 탐색
def find_location(n):
    min_loc, max_loc = 1, len(ascending_arr)-1 # 0번째와 마지막은 제외
    while min_loc < max_loc:
        mid = min_loc + (max_loc -  min_loc)//2
        if ascending_arr[mid] < n:
            min_loc = mid + 1
        else:
            max_loc = mid

    return max_loc

# 입력
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

ascending_arr = [0]
for a in arr:
    if ascending_arr[-1] < a:
        # 마지막으로 추가한 숫자보다 클 경우 증가하는 수열에 추가
        ascending_arr.append(a)  
    else:
        # 마지막으로 추가한 숫자보다 작을 경우 들어갈 자리를 찾음
        # 그 자리를 a로 교체(더 작은 숫자가 들어가게 됨)
        ascending_arr[find_location(a)] = a

print(len(ascending_arr)-1) # 0제외
