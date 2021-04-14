# https://www.acmicpc.net/problem/2110

import sys

def cut(height):
    result = 0
    for t in trees:
        result += max(t-height, 0)
    return result

# 입력
N, C = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))