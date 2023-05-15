import sys
input = sys.stdin.readline

def makeZero(s):
    n = int(s[-1])
    if n == N:
        if eval(s.replace(" ", "")) == 0:
            print(s)
        return

    for e in exp:
        makeZero(s+e+str(n+1))


T = int(input())
exp = [" ", "+", "-"]
for _ in range(T):
    N = int(input())
    makeZero("1")
    print()
