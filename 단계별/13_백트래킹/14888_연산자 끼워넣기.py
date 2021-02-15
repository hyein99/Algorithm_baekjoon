import sys

def operate(op, x, y):
    if op==0:
        return x+y
    elif op==1:
        return x-y
    elif op==2:
        return x*y
    else:
        if x<0 and y>0:
            return (-x)//y*(-1)
        return x//y

def is_available(oplist, op): # oplist: 남은 op 리스트, op: 테스트할 op 인덱스
    # op가 남아있는지 확인
    if oplist[op] == 0:
        return False
    return True

def DFS(n, cnt):  # n: 계산 중간값, cnt: 연산개수
    global maxn, minn
    if cnt == len(arr)-1:
        # print(f'계산결과: {n}')
        if n > maxn:
            maxn = n
        if n < minn:
            minn = n
        return
    for idx in range(len(oplist)): # idx: 연산자 리스트 인덱스
        if is_available(oplist, idx):
            oplist[idx] -= 1
            m = operate(idx, n, arr[cnt+1])
            # print(f'연산자: {idx}, {n}>{m}')
            DFS(m, cnt+1)
            oplist[idx] += 1


# 입력
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
oplist = list(map(int, sys.stdin.readline().split()))

maxn = -1000000000
minn = 1000000000
DFS(arr[0], 0)
print(maxn)
print(minn)