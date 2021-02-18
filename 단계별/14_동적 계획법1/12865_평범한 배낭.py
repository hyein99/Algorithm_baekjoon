import sys

def pack_knapsack(cargo, cap):
    pack=[]

    for i in range(len(cargo)+1):
        pack.append([])
        for c in range(cap+1):
            if i==0 or c==0:
                pack[i].append(0)
            elif cargo[i-1][0] <= c: # 짐을 추가할 수 있는 경우
                pack[i].append(
                    max(
                        cargo[i-1][1] + pack[i-1][c-cargo[i-1][0]],
                        pack[i - 1][c]
                    )
                )
            else:
                pack[i].append(pack[i-1][c])
    return pack[-1][-1]

# 입력
N, K = map(int, sys.stdin.readline().split())
cargo = [] # (무게, 가치)
for _ in range(N):
    cargo.append(list(map(int, sys.stdin.readline().split())))

print(pack_knapsack(cargo, K))