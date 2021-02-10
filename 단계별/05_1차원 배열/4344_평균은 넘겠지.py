import sys

n = int(sys.stdin.readline())
for i in range(n):
    arr = list(map(int, input().split()))
    std = arr[0]
    glst = arr[1:]
    cnt = 0
    for g in glst:
        if g > sum(glst)/len(glst):
            cnt += 1
    print('{:.3f}%'.format(cnt/std*100))