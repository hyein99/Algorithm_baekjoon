import sys

while True:
    sent = sys.stdin.readline().rstrip()
    if sent == '.':
        break

    vlist = []
    vstr = list(sent)
    while vstr:
        # print(vstr)
        v = vstr.pop(0)
        if v == '(' or v == '[':
            vlist.append(v)
        elif v == ')' or v == ']':
            if len(vlist) == 0:
                print('no')
                vstr.append(v) # 마지막에 나왔을 경우 대비
                break
            else:
                x = vlist.pop()
                if (x=='(' and v==']') or (x=='[' and v==')'):
                    print('no')
                    vstr.append(v)
                    vlist.append(x)
                    break

    if len(vstr) == 0:
        if len(vlist) == 0:
            print('yes')
        else:
            print('no')

