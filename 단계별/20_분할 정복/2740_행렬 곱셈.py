import sys

def multiply_matrix(A, B):
    for i in range(len(A)):
        X = A[i]
        for j in range(len(B[0])):
            Y = [row[j] for row in B]
            print(sum(x*y for x, y in zip(X, Y)), end=' ')
        print()

# 입력
N, M = map(int, sys.stdin.readline().split())
A = []
for _ in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))
N, M = map(int, sys.stdin.readline().split())
B = []
for _ in range(N):
    B.append(list(map(int, sys.stdin.readline().split())))

multiply_matrix(A, B)