import sys
from collections import deque

T = int(sys.stdin.readline())
for _ in range(T):
    fd = list(sys.stdin.readline())
    n = int(sys.stdin.readline())
    nstr = sys.stdin.readline().strip("[]\n")
    nd = deque(nstr.split(',')) if nstr else deque()
    reverse = False
    error = False
    for f in fd:
        if f == 'R':
            reverse = not reverse
        elif f == 'D':
            if nd:
                nd.popleft() if not reverse else nd.pop()
            else:
                error = not error
                break
    if reverse:
        nd.reverse()

    if not error:
        print('['+','.join(nd)+']')
    else:
        print('error')