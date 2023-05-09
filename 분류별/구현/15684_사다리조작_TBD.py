# def add_ladder(i, j, cnt):
#     # print(i,j,cnt)
#     global result
#     if cnt > 3:
#         return
#     if check_result():
#         result = min(result, cnt)
#         return
#
#     for h in range(i, H+1):
#         if h == i:
#             for n in range(j, N):
#                 if ladder[h][n] == 0:
#                     ladder[h][n] = 1
#                     add_ladder(h, n, cnt+1)
#                     ladder[h][n] = 0
#         else:
#             for n in range(1, N):
#                 if ladder[h][n] == 0:
#                     ladder[h][n] = 1
#                     add_ladder(h, n, cnt+1)
#                     ladder[h][n] = 0
#
#
# def check_result():
#     for i in range(1, N):
#         l = i
#         for j in range(1, H+1):
#             if ladder[j][l] == 1:  # 오른쪽으로
#                 l += 1
#             elif ladder[j][l-1] == 1:  # 왼쪽으로
#                 l -= 1
#         if l != i: # i 세로선 결과가 i번이 아닐때
#             return False
#     return True
#
#
# # 입력
# N, M, H = map(int, input().split())
# ladder = [[0 for _ in range(N+1)] for _ in range(H+1)]
# for _ in range(M):
#     a, b = map(int, input().split())
#     ladder[a][b] = 1
# print(*ladder, sep='\n')
#
# result = 4
# add_ladder(1, 1, 0)
# if result > 3:
#     print(-1)
# else:
#     print(result)