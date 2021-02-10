def star(n):
    global slist

    if n==3:   # 최소 모형 단위
        slist[0][:3] = slist[2][:3] = ['*']*3
        slist[1][:3] = ['*', ' ', '*']
        return
    x = n//3   # 별 찍는 단위가 될 수
    star(x)
    for i in range(3):
        for j in range(3):
            if i==1 and j==1:
                continue
            for k in range(x):
                slist[x*i+k][x*j:x*(j+1)] = slist[k][:x]


N = int(input())
slist = [[' ' for i in range(N)] for i in range(N)]
star(N)
for sl in slist:
    for s in sl:
        print(s, end='')
    print()