n, m = map(int, input().split())
cards = list(map(int, input().split()))

max = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            csum = cards[i]+cards[j]+cards[k]
            if csum > max and csum <= m:
                max = csum
print(max)