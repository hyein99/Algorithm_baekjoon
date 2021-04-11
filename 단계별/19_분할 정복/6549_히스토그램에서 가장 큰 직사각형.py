import sys
from collections import defaultdict
from collections import deque

# 풀이 1) 완전탐색(?) > 시간초과
# # idx번째 높이 기준으로 만들 수 있는 최대 직사각형
# def get_max_area(height, idx):
#     area = height
#     # idx기준 왼쪽
#     for i in range(idx-1, 0, -1):
#         if arr[i] < height:
#             break
#         area += height
#
#     # idx기준 오른쪽
#     for i in range(idx+1, len(arr)):
#         if arr[i] < height:
#             break
#         area += height
#
#     return area
#
#
# while True:
#     arr = list(map(int, sys.stdin.readline().split()))
#     if arr == [0]:
#         break
#
#     maxsquare = defaultdict(int)
#     result = 0
#     for i in range(1, len(arr)):
#         height = arr[i]
#         if not maxsquare[height]:
#             maxsquare[height] = get_max_area(height, i)
#             result = max(result, maxsquare[height])
#
#     print(result)


# 풀이 2) stack 활용
while True:
    n, *heights = list(map(int, sys.stdin.readline().split()))
    if n == 0:
        break

    # 첫 시점 + heights + 마지막 사각형
    heights = [-1] + heights + [-1] # 넓이라서 0이 상관없지만 -1로 풀어야 더 정확함!!!!!
    st = deque()  # 체크 완료한 height의 idx
    max_area = 0

    print(heights)
    for i in range(n+2):
        print(f'i: {i}')
        # heights[i]: current_height
        # heights[st[-1]]: previous_height
        # previous_height > current_height이면(while) area 계산 이어갈 수 없음
        print(st)
        while st and heights[st[-1]] > heights[i]:
            print(f'previous: {heights[st[-1]]}, current: {heights[i]}')
            previous_idx = st.pop()
            # 지금까지 저장된 사각형 높이 계산
            # i: current_idx (current보다 -1까지가 높이보다 작은 범위)
            # st[-1]: ???
            # i-1-st[-1]: 저장할 가로 길이
            print(f'st[-1]: {st[-1]}, 가로: {i-1-st[-1]}, 세로: {heights[previous_idx]}')
            area = (i-1-st[-1]) * heights[previous_idx]
            max_area = max(area, max_area)
        st.append(i)

    print(max_area)