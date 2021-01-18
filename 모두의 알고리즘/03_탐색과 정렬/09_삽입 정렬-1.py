# Version.1: 쉽게 설명한 삽입 정렬 알고리즘

# 리스트 r에서 v가 들어가야 할 위치를 돌려주는 함수
def find_ins_idx(r, v):
    a = len(r)
    for i in range(a):
        if v < r[i]:
            return i
    return a

def ins_sort(r):
    result = []
    while r:
        value = r.pop(0)
        ins_idx = find_ins_idx(result, value)
        result.insert(ins_idx, value)
    return result

d = [2, 4, 5, 1, 3]
print(ins_sort(d))