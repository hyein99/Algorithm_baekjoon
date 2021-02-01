# 미로 탈출 방법이 한 가지가 아니일 때

def solve_maze(g, start, end):
    qu = []       # 앞으로 처리해야 할 이동 경로
    done = set()  # 이미 추가한 꼭짓점들

    qu.append(start)
    done.add(start)

    while  qu:
        p = qu.pop(0) # 처리해야할 경로
        v = p[-1]     # 이동경로 p의 마지막 문자가 현재 처리해야할 꼭짓점
        # print(p)
        if v == end:
            # return p
            print('answer:', end=' ')
            print(p)
        for x in g[v]:
            if x not in p:
                qu.append(p+x)
                done.add(x)

    # return '?'
    print('?')


maze2 = {
    'a':['e'],
    'b':['c', 'f'],
    'c':['b', 'd'],
    'd':['c'],
    'e':['a', 'i'],
    'f':['b', 'g', 'j'],
    'g':['f', 'h'],
    'h':['g', 'l'],
    'i':['e', 'm', 'j'], # i>j 연결
    'j':['f', 'k', 'n', 'i'],
    'k':['j', 'o'],
    'l':['h', 'p'],
    'm':['i', 'n'],
    'n':['m', 'j'],
    'o':['k'],
    'p':['l']
}

solve_maze(maze2, 'a', 'p')