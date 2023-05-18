import re

T = int(input())
for _ in range(T):
    s = input()
    if None == re.fullmatch(r"((100+1+)|(01))+", s):
        print('NO')
    else:
        print('YES')