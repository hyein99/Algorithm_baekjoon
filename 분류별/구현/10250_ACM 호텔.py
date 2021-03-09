# https://www.acmicpc.net/problem/10250

import sys

T = int(sys.stdin.readline())
for _ in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    ho = (N%H*100)+(N//H+1) if N%H else (H*100)+(N//H)
    print(ho)