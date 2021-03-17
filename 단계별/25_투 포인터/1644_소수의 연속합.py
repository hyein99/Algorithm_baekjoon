import sys

def get_primenumber(N):
    num = [True]*(N+1)
    num[0] = num[1] = 0
    for i in range(2, N+1):
        if num[i]:
            t = 2
            while i*t <= N:
                num[i*t] = 0
                t += 1
    prime = sorted([i for i in range(2, N+1) if num[i]])
    return prime

def get_primesum(N):
    if N==1:
        return 0
    result, l, r = 0, 0, 0
    psum = prime[0]
    while r < len(prime):
        if psum < N:
            r += 1
            if r < len(prime):
                psum += prime[r]
        elif psum > N:
            psum -= prime[l]
            l += 1
        else:
            result += 1
            if r + 1 < len(prime):
                psum = psum + prime[r + 1] - prime[l]
            r += 1
            l += 1
    return result

N = int(sys.stdin.readline())

# 소수 리스트 만들기
prime = sorted(list(get_primenumber(N)))
print(get_primesum(N))
