def isSame(arr):
    return True

# 입력
N = int(input()) # 표본 모양 수열의 길이
population = list(map(int, input().split()))

# sample이 될 수 있는 candidate 생성



M = int(input()) # 모양 수열 개수
answer = []
for _ in range(M):
    sample = list(map(int, input().split()))
    if isSame(sample):
        answer.append(sample)

# 출력
print(len(answer))
for i in range(len(answer)):
    print(*answer[i])