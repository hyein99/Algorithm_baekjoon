# https://www.acmicpc.net/problem/1193

import sys

X = int(sys.stdin.readline())
mo = 1
while X > mo:
    X -= mo
    mo += 1
if mo%2:
    print(f'{mo - X + 1}/{X}')

else:
    print(f'{X}/{mo - X + 1}')