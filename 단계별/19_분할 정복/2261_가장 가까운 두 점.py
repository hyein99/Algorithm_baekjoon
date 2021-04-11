import sys

# 시간초과!!!!!!!!!!!!
# # 입력
# n = int(sys.stdin.readline())
# points = []
# for _ in range(n):
#     x, y = map(int, sys.stdin.readline().split())
#     points.append((x, y))
#
# min_length = sys.maxsize
# for i in range(len(points)):
#     for j in range(i+1, len(points)):
#         length = abs(points[i][0]-points[j][0])**2 + abs(points[i][1]-points[j][1])**2
#         min_length = min(min_length, length)
# print(min_length)