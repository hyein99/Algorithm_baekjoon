import sys

N = int(sys.stdin.readline())
dist = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split())) # len(dist)+1

p, total = 0,0,
for i in range(len(dist)):
    if price[p] > price[i]:
        p = i
    total += price[p]*dist[i] # oil은 그대로 0
print(total)