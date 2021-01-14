def star(n):
    if n==3:
        s = '*'
    else:
        s = 3*star(n//3)
    return s*3+'\n'+s+' '+s+'\n'+s*3

print(star(9))
