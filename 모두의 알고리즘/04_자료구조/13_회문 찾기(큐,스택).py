# 회문: 순서대로 읽어도 거꾸로 읽어도 그 내용이 같은 낱말이나 문장

def palindrome(s):
    qu = []
    st = []

    # 1단계: 문자열의 알파벳 문자를 각각 큐와 스택에 넣음
    for x in s:
        if x.isalpha(): # 공백, 숫자, 특수문자가 아니면
            qu.append(x.lower())
            st.append(x.lower())
    # 2단계: 큐와 스택에서 꺼낸 문자를 비교
    while qu:
        if qu.pop(0) != st.pop():
            return False
    return True

print(palindrome('Wow'))
print(palindrome("Madam, I'm Adam."))
print(palindrome('Madam, I am Adam.'))

### collections 모듈 사용하기
from collections import deque
qu1 = deque()
qu1.append(1)
qu1.append(2)
qu1.popleft()
print(qu1)