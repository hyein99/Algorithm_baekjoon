import sys

num = ''
result = 0
op = ''
for e in sys.stdin.readline():
    if e.isdigit():
        num += e
    else:
        if op == '-':
            result -= int(num)
            op = '-'
        else:
            result += int(num)
            op = e
        num = ''
print(result)

# 55+50+40
# 55+50-40
# 55-50+40
# 55-50-40