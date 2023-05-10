# https://www.acmicpc.net/problem/14889

INF = int(1e7)
def split_team(start, idx):
    global min_diff
    if len(start) == N//2:
        # step 2: calculate difference btw s, l
        # print(start)
        link = list(total-set(start))
        diff = abs(get_score(start) - get_score(link))
        # print(get_score(start), get_score(link))
        min_diff = min(min_diff, diff)
        return

    for i in range(idx, N):
        split_team(start+[i], i+1)


def get_score(team):
    score = 0
    for i in range(N//2):
        a = team[i]
        for j in range(i+1, N//2):
            b = team[j]
            score += arr[a][b] + arr[b][a]
    return score


# input
N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

min_diff = INF
total = set([i for i in range(N)])

# step 1: split team into s, l
split_team([], 0)

# output
print(min_diff)
