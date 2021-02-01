# 최대 수익 알고리즘
# 1) 한 번 반복으로 최대 수익 찾기
# 계산복잡도: O(n)

def max_profit(prices):
    n = len(prices)
    maxpf = 0
    minpr = prices[0]

    for i in range(1, n):
        pf = prices[i] - minpr
        if pf > maxpf:
            maxpf = pf
        if prices[i] < minpr:
            minpr = prices[i]
    return maxpf

stock = [10300, 9600, 9800, 8200, 7800, 8300, 9500, 9800, 10200, 9500]
print(max_profit(stock))