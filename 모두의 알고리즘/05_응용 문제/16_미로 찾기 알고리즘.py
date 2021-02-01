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
            return p
        for x in g[v]:
            if x not in done:
                qu.append(p+x)
                done.add(x)

    return '?'
maze = {
    'a':['e'],
    'b':['c', 'f'],
    'c':['b', 'd'],
    'd':['c'],
    'e':['a', 'i'],
    'f':['b', 'g', 'j'],
    'g':['f', 'h'],
    'h':['g', 'l'],
    'i':['e', 'm'],
    'j':['f', 'k', 'n'],
    'k':['j', 'o'],
    'l':['h', 'p'],
    'm':['i', 'n'],
    'n':['m', 'j'],
    'o':['k'],
    'p':['l']
}


print(solve_maze(maze, 'a', 'p'))