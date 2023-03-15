import sys
import heapq
input = sys.stdin.readline

# 입력
N, K = map(int, input().split())
jewel = []
for _ in range(N):
    m, v = map(int, input().split())  # 무게, 가격
    heapq.heappush(jewel, (m, v))
bag = []  # 수용 무게 적은 순(가성비)
for _ in range(K):
    bag.append(int(input()))
bag.sort()

cand = []
answer = 0
for c in bag:
    while jewel:
        m, v = heapq.heappop(jewel)
        if c >= m:
            heapq.heappush(cand, -v)  # 비싼거 부터 뽑기 위해
        else:  # 가벼운 순서로 정렬되어 있어서 뒤에 안봐도 됨
            heapq.heappush(jewel, (m, v))
            break

    if cand:  # c보다 무게 작은 보석들
        answer -= heapq.heappop(cand)  # 음수로 넣었으니까 -

# 출력
print(answer)


# 보석: 비싸고 가벼운 순
# 가방: 가벼운 것 부터
# >> 이 가방에 들어갈 수 있는 가장 비싼거
# bag pop
# jewel for loop >> heap을 쓰려면! 가벼운 순서대로 해서 뽑아서 가능한 후보 만들기
# bag >= jewel: answer +, jewel 팔림