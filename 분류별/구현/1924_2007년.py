import sys

mm, dd = map(int, sys.stdin.readline().split())
dsum = dd
for m in range(1, mm):
    if m in [1,3,5,7,8,10,12]:
        dsum += 31
    elif m in [4,6,9,11]:
        dsum += 30
    else:
        dsum += 28

if dsum%7==1:
    print('MON')
elif dsum%7==2:
    print('TUE')
elif dsum%7==3:
    print('WED')
elif dsum%7==4:
    print('THU')
elif dsum%7==5:
    print('FRI')
elif dsum%7==6:
    print('SAT')
else:
    print('SUN')