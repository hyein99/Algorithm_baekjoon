# https://www.acmicpc.net/problem/10816

import sys
from collections import Counter

# 풀이 1) Counter 사용
# # 입력
# N = int(sys.stdin.readline())
# cards = list(map(int, sys.stdin.readline().split()))
# M = int(sys.stdin.readline())
# arr = list(map(int, sys.stdin.readline().split()))
#
# card_number = Counter(cards)
# for a in arr:
#     print(card_number[a], end=' ')

# 풀이 2) 이분탐색
def bin_search(target):
    left, right = 0, len(cards) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if cards[mid] < target:
            left = mid + 1
        elif cards[mid] > target:
            right = mid - 1
        else:
            # target이 있는 범위내에서 count
            return cards[left:right+1].count(target)
    return 0

# 입력
N = int(sys.stdin.readline())
cards = sorted(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
arr = map(int, sys.stdin.readline().split())

ndict = dict()
for a in arr:
    if a not in ndict:
        ndict[a] = bin_search(a)
    print(ndict[a], end=' ')
