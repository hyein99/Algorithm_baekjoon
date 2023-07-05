def isPPAP(s):
    done = []
    for i in range(len(s)):
        done.append(s[i])
        if len(done) >= 4 and done[-4:] == PPAP:
            for _ in range(3):
                done.pop()
    if done == ['P'] or done == PPAP:
        return 'PPAP'
    else:
        return 'NP'


# input
PPAP = ['P', 'P', 'A', 'P']
S = input()
print(isPPAP(S))
