####### case 1) heqpq를 통한 greedy
import heapq

# 입력
N = int(input())
cards = []
for _ in range(N):
    heapq.heappush(cards, int(input()))

answer = 0
if N > 1:
    while len(cards) > 1:
        a = heapq.heappop(cards)
        b = heapq.heappop(cards)
        answer += (a+b)
        heapq.heappush(cards, a+b)

print(answer)