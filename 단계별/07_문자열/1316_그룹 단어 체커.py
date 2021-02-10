num = int(input())

cnt = num
for _ in range(num):
    word = list(input())

    rep = word[0]
    alpha = [rep]
    for w in word:
        if w != rep:
            if w in alpha:
                cnt -= 1
                break
            rep = w
            alpha.append(rep)

print(cnt)

# find: index 반환(시간복잡도 높음)
