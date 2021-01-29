def gcd(a, b):
    i = min(a, b)
    while True:
        if a % i == 0 and b % i == 0:
            return i
        i -= 1

print(gcd(1, 5))
print(gcd(3, 6))
print(gcd(60, 24))
print(gcd(81, 27))


# 유클리드 방식(재귀)을 이용해 최대공약수를 구하는 알고리즘
def gcd2(a, b):
    if b == 0:
        return a
    return gcd2(b, a%b)

print(gcd2(1, 5))
print(gcd2(3, 6))
print(gcd2(60, 24))
print(gcd2(81, 27))