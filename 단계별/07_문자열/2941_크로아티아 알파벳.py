word = input()
calpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

cnt = 0
for c in calpha:
    cc = word.count(c)
    cnt += cc
    word = word.replace(c, ' ')
word = word.replace(' ', '')
cnt += len(word)
print(cnt)