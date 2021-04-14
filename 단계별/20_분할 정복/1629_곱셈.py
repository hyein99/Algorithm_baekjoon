import sys

def multiply(A, B, C):
    result = 1
    while B >= 1:
        tmp = A%C
        if B%2:
            result *= tmp
            result %= C
        B //= 2
        A = tmp*tmp
    return result

A, B, C = map(int, sys.stdin.readline().split())
print(multiply(A, B, C))
