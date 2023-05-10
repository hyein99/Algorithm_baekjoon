def is_available(r):
    for i in range(r):
        if board[i] == board[r] or abs(r-i) == abs(board[r]-board[i]):
            return False
    return True


def DFS(cur_row):
    global cnt

    if cur_row == N:
        cnt += 1
        return

    for cur_col in range(N):
        board[cur_row] = cur_col  # cur_row의 cur_col에 queen
        if is_available(cur_row):
            visited[cur_col] = True
            DFS(cur_row + 1)
            visited[cur_col] = False


N = int(input())
board = [0] * N
visited = [False] * N
cnt = 0

DFS(0)
print(cnt)