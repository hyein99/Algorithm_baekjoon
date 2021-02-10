year = int(input())

# if ((year%4 == 0) & (year%100 != 0)) | (year%400 == 0):
if (~(year % 4) and (year % 100)) or ~(year % 400):
    print(1)
else:
    print(0)