# input
T = int(input())
for _ in range(T):
    W = input()
    K = int(input())
    word_dict = dict()
    min_s, max_s = int(1e9), -1
    for i in range(len(W)):
        if W[i] in word_dict:
            word_dict[W[i]].append(i)
        else:
            word_dict[W[i]] = [i]
        l = len(word_dict[W[i]])
        if l >= K:
            min_s = min(min_s, i - word_dict[W[i]][l - K] + 1)
            max_s = max(max_s, i - word_dict[W[i]][l - K] + 1)
    # output
    if max_s == -1:
        print(-1)
    else:
        print(min_s, max_s)