import sys

N = int(sys.stdin.readline())
nlist = []
for _ in range(N):
    nlist.append(int(sys.stdin.readline()))

st = []
i = 1
j = 0
result = []
while j < N:
    n = nlist[j]
    if n > i:
        st.append(i)
        result.append('+')
        i += 1
    elif n == i:
        result.append('+')
        result.append('-')
        i += 1
        j += 1
    else:
        x = st.pop()
        if x != n:
            result = ['NO']
            break
        result.append('-')
        j += 1

print(*result, sep='\n')
