from collections import deque

# 입력
N, K = map(int, input().split())
device = list(map(int, input().split()))

# 각 device가 언제 등장하는지 구해놓기
device_order = [deque() for _ in range(K+1)]  # device_order[1]
for i in range(K):
    device_order[device[i]].append(i)

useYN = [0 for _ in range(K+1)]  # useYN[1]
tab_cnt = 0
answer = 0
for i in range(K):
    print(i, device[i])
    device_order[device[i]].popleft()
    print(useYN)
    if useYN[device[i]] == 1:  # 이미 꽂아 있는 경우
        continue

    if tab_cnt < N:  # 멀티탭 공간 있는 경우
        tab_cnt += 1
        useYN[device[i]] = 1
    else:
        pull_device = -1
        max_dist = 0  # 제일 늦게 등장하는 거 뽑기
        for j in range(1, K+1):
            if useYN[j] == 1:  # 꽂아 있는 용품 중
                if len(device_order[j]) == 0:  # 앞으로 등장안하면 뽑아도 됨
                    pull_device = j
                    break
                elif device_order[j][0] > max_dist:
                    max_dist = device_order[j][0]
                    pull_device = j
        # device_order[pull_device].popleft()

        print('pull', pull_device)
        useYN[pull_device] = 0
        useYN[device[i]] = 1
        answer += 1

# 출력
print(answer)

# 3 12
# 1 2 3 1 2 4 1 3 3 1 2 4  > 왜 4 뽑지?!

#          (2):134
#                    (4):
#                      (1):234