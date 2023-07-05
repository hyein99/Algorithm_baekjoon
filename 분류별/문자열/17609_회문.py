def isPalin(s, left, right):
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            if subPalin(s, left+1, right) or subPalin(s, left, right-1):
                return 1
            else:
                return 2
    return 0


def subPalin(s, left, right):
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


# input
T = int(input())
for _ in range(T):
    s = input()
    print(isPalin(s, 0, len(s)-1))
