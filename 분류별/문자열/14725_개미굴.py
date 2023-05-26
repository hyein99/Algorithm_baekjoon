import sys
input = sys.stdin.readline

def fill_dict(d, i):
    if i == len(arr):
        return d

    if arr[i] not in d:
        d[arr[i]] = {}
    d[arr[i]] = fill_dict(d[arr[i]], i+1)
    return d


def print_dict(d, cnt):
    l = sorted(d)
    for i in range(len(l)):
        print('--'*cnt + l[i])
        print_dict(d[l[i]], cnt+1)

N = int(input().strip())
ant_dict = {}
for _ in range(N):
    arr = list(input().strip().split())
    K = int(arr[0])

    ant_dict = fill_dict(ant_dict, 1)

print_dict(ant_dict, 0)
