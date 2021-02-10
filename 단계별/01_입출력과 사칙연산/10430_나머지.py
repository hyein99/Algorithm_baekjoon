A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)

x1 = (A+B)%C
x2 = ((A%C) + (B%C))%C
x3 = (A*B)%C
x4 = ((A%C)*(B%C))%C

print('{}\n{}\n{}\n{}'.format(x1, x2, x3, x4))