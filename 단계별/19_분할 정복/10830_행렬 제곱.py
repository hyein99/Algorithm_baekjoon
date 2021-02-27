import sys

def index_matrix(arr):
    result = [[0]*len(arr) for _ in range(len(arr))]
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i==j:
                result[i][j] = 1
    return result

def multiple_matrix(A, B):
    result = []
    for i in range(len(A)):
        X = A[i]
        tmp = []
        for j in range(len(B[0])):
            Y = [row[j] for row in B]
            tmp.append(sum(x*y for x, y in zip(X, Y))%1000)
        result.append(tmp)
    return result

def square_matrix(arr, B):
    result = index_matrix(arr)
    while B >=1:
        if B%2:
            result = multiple_matrix(result, arr)
        B //= 2
        arr = multiple_matrix(arr, arr)

    return result



# 입력
N, B = map(int, sys.stdin.readline().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

result = square_matrix(arr, B)
for i in range(len(result)):
    print(*result[i], sep=' ')