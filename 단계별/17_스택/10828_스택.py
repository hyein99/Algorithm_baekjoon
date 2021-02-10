import sys

N = int(sys.stdin.readline())
slist = []
for _ in range(N):
    order = list(sys.stdin.readline().split())
    if order[0] == 'push':
        slist.append(int(order[1]))
    elif order[0] == 'pop':
        if len(slist) > 0:
            print(slist.pop())
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(slist))
    elif order[0] == 'empty':
        if slist:
            print(0)
        else:
            print(1)
    else:
        if len(slist) > 0:
            print(slist[len(slist)-1])
        else:
            print(-1)


