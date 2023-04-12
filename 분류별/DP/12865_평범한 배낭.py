# 입력
N, K = map(int, input().split())  # 물품 수, 버틸 수 있는 무게
arr = []
for _ in range(N):
    W, V = map(int, input().split())  # 무게, 가치
    arr.append((W, V))

# 출력
pack = []
for i in range(N+1):
    pack.append([])
    for j in range(K+1):
        if i==0 or j==0:
            pack[i].append(0)
        elif arr[i-1][0] <= j:  # i 번재 물건 들어감
            pack[i].append(
                max(pack[i-1][j-arr[i-1][0]] + arr[i-1][1],
                    pack[i-1][j])  # i 번째 물건 안넣음
            )
        else:
            pack[i].append(pack[i-1][j])

print(pack[-1][-1])