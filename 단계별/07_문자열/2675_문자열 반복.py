n = int(input())

for i in range(n):
    test = input().split()
    cnt = int(test[0])
    word = list(test[1])
    for w in word:
        print(w*cnt, end='')
    print()