def hanoi(n, fr, to, sub):
    if n == 1:
        print(fr, '->', to)
        return

    # 원반 n-1개를 sub기둥으로 이동
    hanoi(n-1, fr, sub, to)
    # 가장 큰 원반을 to기둥으로 이동
    print(fr, '->', to)
    # sub기둥에 옮긴 n-1개의 원반을 to기둥으로 이동
    hanoi(n-1, sub, to, fr)

print('n=1')
hanoi(1, 1, 3, 2)
print('-'*30)
print('n=2')
hanoi(2, 1, 3, 2)
print('-'*30)
print('n=3')
hanoi(3, 1, 3, 2)
