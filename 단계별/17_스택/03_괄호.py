import sys

N = int(sys.stdin.readline())
for _ in range(N):
    vlist = []
    vstr = list(sys.stdin.readline().rstrip())
    while vstr:
        # print(vstr)
        v = vstr.pop(0)
        if v == '(':
            vlist.append(v)
        else:
            if len(vlist) == 0:
                print('NO')
                vstr.append(v)
                break
            else:
                vlist.pop()
    if len(vstr)==0:
        if len(vlist)==0:
            print('YES')
        else:
            print('NO')