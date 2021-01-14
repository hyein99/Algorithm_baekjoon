N = int(input())
big = []
ord = [1]*N
for i in range(N):
    big.append(list(map(int, input().split())))
    for j in range(i, 0, -1):
        if big[i][0] > big[j-1][0] and big[i][1] > big[j-1][1]:
            ord[j-1] += 1
        elif big[i][0] < big[j-1][0] and big[i][1] < big[j-1][1]:
            ord[i] += 1
print(*ord, sep=' ')
