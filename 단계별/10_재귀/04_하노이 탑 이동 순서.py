def times(n):
    if n==1:
        return 1
    else:
        return 2**(n-1)+times(n-1)

def orders(n):
    i=3
    if n==1:
        print('1', i)
    elif n==2:
        print('1 2')
        print('1 3')
        print('2 3')




orders(1)

# 1:1 (1>3)
# 2:3 (1>2, 1>3, 2>3)
# 3:7 (1>3, 1>2, 3>2, 1>3, 2>1, 2>3, 1>3)
# 4:15(1>2, 1>3, 2>3, 1>2, 3>1, 3>2, 1>2, 1>3, 2>3, 2>1, 3>1, 2>3, 1>2, 2>3, 1>3)