def kmp(pattern):
    table = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j-1]
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j
    return max(table)


alpha = input()
max_length = 0
for idx in range(len(alpha)):
    max_length = max(kmp(alpha[idx:len(alpha)]), max_length)

print(max_length)