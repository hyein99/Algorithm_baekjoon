import sys
from collections import defaultdict

dp = defaultdict(int)
def w(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif dp[(a,b,c)]:
        return dp[(a,b,c)]
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    elif a < b and b < c:
        dp[(a,b,c)] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dp[(a,b,c)]
    else:
        dp[(a, b, c)] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return dp[(a,b,c)]

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a==b==c==-1:
        break
    result = w(a,b,c)
    print(f'w({a}, {b}, {c}) = {result}')