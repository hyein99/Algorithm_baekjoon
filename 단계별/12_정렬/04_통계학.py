import sys
from collections import Counter

N = int(sys.stdin.readline())

nlist = []
for _ in range(N):
    nlist.append(int(sys.stdin.readline()))
nlist.sort()

# 최빈값구하기
cnt = Counter(nlist).most_common()
if len(cnt) > 1 and cnt[0][1] == cnt[1][1]:
    freq = cnt[1][0]
else:
    freq = cnt[0][0]

print(round(sum(nlist)/len(nlist)))
print(nlist[len(nlist)//2])
print(freq)
print(nlist[-1]-nlist[0])