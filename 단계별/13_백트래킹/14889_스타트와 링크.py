import sys

def is_availalbe(team):
    # 팀원 다 찼는지
    if len(team) == N/2:
        return False
    return True


def get_diff(start, link):
    tw_st = 0
    tw_lk = 0
    for i in start:
        for j in start:
            tw_st += synergy[i][j]
    for i in link:
        for j in link:
            tw_lk += synergy[i][j]
    return abs(tw_st-tw_lk)


def DFS(remain, start, link):
    global mindiff
    if remain == 0:
        diff = get_diff(start, link)
        if diff < mindiff:
            mindiff = diff
        return

    for i in range(2):
        if i==0:
            if is_availalbe(start):
                start.append(N-remain) # N-remain번째 사람 배치
                DFS(remain - 1, start, link)
                start.pop()
        else:
            if is_availalbe(link):
                link.append(N - remain)  # N-remain번째 사람 배치
                DFS(remain - 1, start, link)
                link.pop()


# 입력
N = int(sys.stdin.readline())
synergy = []
mindiff = 0
for _ in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))
    synergy.append(tmp)
    mindiff += sum(tmp)

DFS(N, [], [])
print(mindiff)