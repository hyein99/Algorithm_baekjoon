N, M = map(int, input().split())

board = []
for i in range(N):
    board.append(list(input()))

minch = 8*8
## h: 0~N-1, w: 0~M-1
for h in range(0, N-7):
    for w in range(0, M-7):

        # sub 체스판
        cnt = 0
        for nh in range(h, h+8):
            for nw in range(w, w+8):
                if (nh+nw)%2==1 and board[nh][nw]=='B':
                    cnt += 1
                elif (nh+nw)%2==0 and board[nh][nw]=='W':
                    cnt += 1
        if min(64-cnt, cnt) < minch:
            minch = min(64-cnt, cnt)
print(minch)