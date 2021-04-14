import sys
from collections import deque

time = int(sys.stdin.readline())

for _ in range(time):
    N, M = map(int, sys.stdin.readline().split())
    imp = deque(map(int, sys.stdin.readline().split()))
    n = 1    # 출력되는 순서
    while True:
        mx = max(imp)      # 남아있는 것들 중 최대값
        x = imp.popleft()
        if mx != x:
            imp.append(x)
            if M == 0:
                M = len(imp)-1
            else:
                M -= 1
        else:
            if M == 0:
                break
            else:
                M -= 1
                n += 1
    print(n)