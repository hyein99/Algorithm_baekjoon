# https://www.acmicpc.net/problem/13325

def dfs(x, s):
    if x == k-1:
        maxx = max(tree[s][s*2], tree[s][s*2+1])
        dp[s] = [maxx, 2*maxx]
    else:
        dp[s][0] = max(tree[s][s*2] + dfs(x+1, s*2)[0],
                       tree[s][s*2+1] + dfs(x+1, s*2+1)[0])
        dp[s][1] = dp[s*2][1] + dp[s*2+1][1] + dp[s][0] - dp[s*2][0] + dp[s][0] - dp[s*2+1][0]
    return dp[s]

# 입력
k = int(input())
arr = list(map(int, input().split()))
tree = {i: {} for i in range(1, 2**(k+1))}  # tree[a][b]=d: a의 자식노드 b까지 거리가 d
for i in range(1, 2**k):
    tree[i][i*2] = arr[(i-1)*2]
    tree[i][i*2+1] = arr[(i-1)*2+1]

dp = [[0, 0] for _ in range(2**(k+1))]
print(dfs(0, 1)[1])