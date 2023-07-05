import re

# input
S = input()
pattern = re.compile('(100+1+|01)+')

if pattern.fullmatch(S):
    print('SUBMARINE')
else:
    print('NOISE')