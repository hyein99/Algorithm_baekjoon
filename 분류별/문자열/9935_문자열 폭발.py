# 모든 폭발 문자열 폭발 > 남은 문자열 이어 붙이기
# 새로 생긴 문자열에 폭발 문자열 포함 > 없을 때까지 폭발
# 마지막 남는 문자열
# 없으면 FRULA

import sys
input = sys.stdin.readline

sentence = input().rstrip()
bomb = list(input().rstrip())
answer = []
for s in sentence:
    answer.append(s)
    if answer[-len(bomb):] == bomb:
        for _ in range(len(bomb)):
            answer.pop()
if answer:
    print(''.join(answer))
else:
    print("FRULA")