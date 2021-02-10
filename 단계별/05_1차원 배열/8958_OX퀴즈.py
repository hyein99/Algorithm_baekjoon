import sys

n = int(sys.stdin.readline())
for i in range(n):
    quiz = sys.stdin.readline()
    sum = 0
    cnt = 0
    for q in quiz:
        if q=='O':
            cnt += 1
            sum += cnt
        else:
            cnt = 0
    print(sum)