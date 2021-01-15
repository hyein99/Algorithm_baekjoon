def times(n):
    if n==1:
        return 1
    else:
        return 2**(n-1)+times(n-1)

def orders(n, fr, to, sub):
    if n==1:
        print(fr, to)
        return
    orders(n-1, fr, sub, to)
    print(fr, to)
    orders(n-1, sub, to, fr)

N = int(input())

print(times(N))
orders(N, 1, 3, 2)