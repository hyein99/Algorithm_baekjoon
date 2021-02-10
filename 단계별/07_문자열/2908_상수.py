x, y = map(int, input().split())
nx = x//100 + x//10%10*10 + x%10*100
ny = y//100 + y//10%10*10 + y%10*100
print(nx if nx > ny else ny)