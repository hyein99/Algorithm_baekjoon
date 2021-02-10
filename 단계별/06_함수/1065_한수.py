# n = int(input())

# cnt = 0
# for i in range(1, n+1):
#     if i < 100:
#         cnt += 1
#         continue
#     elif i < 1000:
#         a1 = i % 10
#         a2 = i // 10 % 10
#         a3 = i // 100 % 10
#         if a1-a2 == a2-a3:
#             cnt += 1
# print(cnt)

###### n자리수의 경우 ============================
n = int(input())

cnt = n
for i in range(1, n+1):
    od = list(str(i))
    if len(od) > 2:
        x = int(od[0]) - int(od[1])
        for j in range(1, len(od)-1):
            if int(od[j]) - int(od[j+1]) != x:
                cnt -= 1
                break

print(cnt)