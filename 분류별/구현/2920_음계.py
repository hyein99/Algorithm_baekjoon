# https://www.acmicpc.net/problem/2920

import sys
code = list(map(int, sys.stdin.readline().split()))
btw = code[1]-code[0]
mflag = False
for i in range(2, 8):
    if code[i]-code[i-1] != btw:
        mflag = True
        break
if mflag:
    print('mixed')
else:
    if btw==1:
        print('ascending')
    else:
        print('descending')