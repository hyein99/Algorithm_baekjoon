# import sys
# from collections import deque
#
# def is_available(cur_col, st):
#     # st: 현재까지 채워진 후보자 리스트(ex len(st)==2면 현재 row=2)
#     cur_row = len(st)
#     for row in range(cur_row):
#         # 수직평가 + 대각선 평가
#         if st[row] == cur_col or abs(st[row]-cur_col) == cur_row - row:
#             return False
#     return True
#
# def DFS(cur_row, st):
#     if len(st)==N:
#         result.append(st[:])
#         return
#
#     for col in range(N):
#         if is_available(col, st):
#             st.append(col)
#             DFS(cur_row+1, st)
#             st.pop()
#
#
# N = int(sys.stdin.readline())
# result = deque()
# DFS(0, [])
# print(len(result))



import sys

def is_available(cur_col):
    # st: 현재까지 채워진 후보자 리스트(ex len(st)==2면 현재 row=2)
    cur_row = len(st)
    for row in range(cur_row):
        # 수직평가 + 대각선 평가
        if st[row] == cur_col or abs(st[row]-cur_col) == cur_row - row:
            return False
    return True

def DFS(cur_row):
    global result
    if len(st)==N:
        result += 1
        return

    for col in range(N):
        if is_available(col):
            st.append(col)
            DFS(cur_row+1)
            st.pop()


N = int(sys.stdin.readline())
result = 0
st = []
DFS(0)
print(result)