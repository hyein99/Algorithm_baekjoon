import sys

n = int(sys.stdin.readline())
x = n
cnt = 0
while True:
    cnt += 1
    a1 = x//10
    a2 = x%10
    x = a2*10 + (a1+a2)%10
    if x == n:
        break
print(cnt)
