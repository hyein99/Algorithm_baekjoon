import sys

# 입력
N = int(sys.stdin.readline())
dist = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split())) # len(dist)+1

p, total = 0,0                 # 기름을 넣을 주유소 번호, 비용
for i in range(len(dist)):
    if price[p] > price[i]:    # 더 싼 가격의 주유소 가격으로 대체
        p = i
    total += price[p]*dist[i]
print(total)