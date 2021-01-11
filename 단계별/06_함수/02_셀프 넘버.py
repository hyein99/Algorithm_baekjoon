d = set(range(1, 10001))

n = 1
while True:
    s = n+(n%10)+(n//10%10)+(n//100%10)+(n//1000%10)+(n//10000%10)
    if s in d:
        d.remove(s)
    if n >= 10000:
        break
    n += 1

print(*d, sep='\n', end='')

# i = 1
# while True:
#     n = i
#     while True:
#         s = n+(n%10)+(n//10%10)+(n//100%10)+(n//1000%10)+(n//10000%10)
#         if s > 10000:
#             break
#         if s in d:
#             d.remove(s)
#         n = s
#     if i >= 10000:
#         break
#     i += 1
#
# for c in d:
#     print(c)