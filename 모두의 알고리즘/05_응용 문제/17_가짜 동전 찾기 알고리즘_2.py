# 가짜 동전 찾기 알고리즘
# 2) 반씩 그룹으로 나누어 비교하기
# 계산 복잡도: O(logn)

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
    # 종료조건: 가짜 동전이 있을 볌위 안에 동전이 한 개 뿐이면 그 동전이 가짜동전
    if left == right:
        return left

    # 동전 그룹나누기
    # 개수가 홀수일 경우 한 개가 남음(right)
    half = (right-left+1)//2
    g1_l = left
    g1_r = left+half-1
    g2_l = left+half
    g2_r = g2_l+half-1

    # 두 그룹 weigh 비교
    result = weigh(g1_l, g1_r, g2_l, g2_r)
    if result == -1:
        return find_fakecoin(g1_l, g1_r)
    elif result == 1:
        return find_fakecoin(g2_l, g2_r)
    else:
        return right # 두 그룹으로 분류되지 않은 동전


n = 100
print(find_fakecoin(0, n-1))