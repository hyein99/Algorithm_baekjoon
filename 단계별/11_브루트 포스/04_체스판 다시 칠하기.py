N, M = map(int, input().split())

board = []
for i in range(N):
    board.append(list(input()))

# ## h: 0~N-1, w: 0~M-1
# for h in range(0, N-7):
#     for w in range(0, M-7):
#         # print(h,'-',h+7,'/',w,'-',w+7)
#         nboard = board[h:h+7][w:w+h]
#         print(nboard)
print(board[0:7][0:7])