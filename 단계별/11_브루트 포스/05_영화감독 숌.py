N = int(input())

cnt = 0
i = 666
while True:
    if '666' in str(i):
        cnt += 1
    if cnt == N:
        print(i)
        break
    i += 1


# 666, 1666, 2666, 3666, 4666, 5666, 6660, 6661, 6662, 6663,
# 6664, 6665, 6666, 6667, 6668, 6669, 7666, 8666, 9666