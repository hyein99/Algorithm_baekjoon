import sys
from collections import defaultdict

# idx번째 높이 기준으로 만들 수 있는 최대 직사각형
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
