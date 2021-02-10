x = int(input())
y = int(input())

a1 = x*(y%10)
a2 = x*(y//10%10)
a3 = x*(y//100)
print('{}\n{}\n{}\n{}'.format(a1, a2, a3, x*y))