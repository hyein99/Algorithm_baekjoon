# 분할 정복을 사용한 거듭제곱과 페르마의 소정리를 이용해 곱셈의 역원을 구하는 문제
# 페르마의 소정리
# a * a^(m-2) = 1 (mod m)
# 이항 계수
# (N K) = N!/K!(N-K)!
# >>> N! * (K!(N-K)!)^(M-2) (mod M)

import sys

def factorial(X):
    result = 1
    if X < 1:
        return 1
    while X!=1:
        result = result * X % M
        X -= 1
    return result


def Nth_power(num, N, mod):
    result = 1
    while N>=1:
        if N%2:
            result = result * num % mod
        N //= 2
        num = num * num % mod
    return result


N, K = map(int, sys.stdin.readline().split())
M = 1000000007

result = factorial(N) * Nth_power(factorial(K)*factorial(N-K), M-2, M) % M
print(result)