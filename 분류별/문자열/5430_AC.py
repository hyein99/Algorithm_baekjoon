from collections import deque
import sys
input = sys.stdin.readline

def RD(p, arr):
    reverse_flag = False
    for s in p:
        if s == 'R':
            reverse_flag = not reverse_flag
        elif s == 'D':
            if arr:
                if reverse_flag:
                    arr.pop()
                else:
                    arr.popleft()
            else:
                return 'error'
    if reverse_flag:
        arr.reverse()
    return '['+','.join(arr)+']'


T = int(input())
for _ in range(T):
    p = list(input())
    n = int(input())
    x = input().strip("[]\n")
    if x:
        arr = deque(x.split(','))
    else:
        arr = deque()
    print(RD(p, arr))