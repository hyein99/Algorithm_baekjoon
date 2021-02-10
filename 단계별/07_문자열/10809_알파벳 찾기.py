word = list(input())
alpha = [-1]*26

for i, w in enumerate(word):
    if alpha[ord(w)-97] == -1:
        alpha[ord(w)-97] = i
print(*alpha)