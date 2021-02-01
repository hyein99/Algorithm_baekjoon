# 모든 친구를 찾아 친밀도를 계산하는 알고리즘

def print_all_friends(g, start):
    qu = []       # 앞으로 처리해야 할 사람들
    done = set()  # 이미 큐에 추가한 사람들(중복 방지)

    qu.append((start, 0)) # (사람이름, 친밀도)를 튜플로 처리
    done.add(start)       # 자기 자신 친밀도: 0

    while qu:
        p, d = qu.pop(0)
        print(p, d)
        for x in g[p]:
            if x not in done:
                qu.append((x, d+1))
                done.add(x)

fr_info = {
    'Summer': ['John', 'Justin', 'Mike'],
    'John': ['Summer', 'Justin'],
    'Justin': ['John', 'Summer', 'Mike', "May"],
    'Mike': ['Summer', 'Justin'],
    'May': ['Justin', 'Kim'],
    'Kim': ['May'],
    'Tom': ['Jerry'],
    'Jerry': ['Tom']
}

print_all_friends(fr_info, 'Summer')
print()
print_all_friends(fr_info, 'Jerry')