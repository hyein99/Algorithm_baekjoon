# 가짜 동전 찾기 알고리즘
# 1) 하나씩 비교하기
# 계산 복잡도: O(n)

# 무게 재는 함수
def weigh(a, b, c, d):
    fake = 29   # 가짜 동전의 위치
    if a <= fake and fake <= b:
        return -1
    elif c <= fake and fake <= d:
        return 1
    else:
        return 0

# 가짜 동전 위치 찾는 함수
def find_fakecoin(left, right):
    for i in range(left+1, right+1):
        result = weigh(left, left, i, i)
        if result == -1: # 왼쪽이 가벼움
            return left
        elif result == 1:
            return i
        # result == 0이면 다음 동전으로
    return -1  # 가짜 동전이 없는 경우

n = 100
print(find_fakecoin(0, n-1))