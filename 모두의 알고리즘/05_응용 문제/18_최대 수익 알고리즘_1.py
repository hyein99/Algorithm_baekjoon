# 최대 수익 알고리즘
# 1) 가능한 모든 경우 비교하기
# 계산복잡도: O(n^2)

def max_profit(prices):
    n = len(prices)
    maxpr = 0

    for i in range(0, n-1):
        for j in range(i+1, n):
            pr = prices[j] - prices[i] # i에 사서 j에 팔았을 때 얻는 수익
            if pr >= maxpr:
                maxpr = pr
    return maxpr

stock = [10300, 9600, 9800, 8200, 7800, 8300, 9500, 9800, 10200, 9500]
print(max_profit(stock))