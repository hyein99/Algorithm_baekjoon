N = list(map(int, list(input())))
N.sort(reverse=True)
print(*N, sep='')