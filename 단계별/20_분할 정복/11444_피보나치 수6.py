# 행렬을 통해 피보나치 계산
# [F(i), F(i-1)] = [[1,1],[1,0]]^i * [F(0), F(1)]

import sys

def multiple_matrix_2(A, B): # 2차원 행렬 곱셈
    mat00 = (A[0][0]*B[0][0] + A[0][1]*B[1][0])%1000000007
    mat01 = (A[0][0]*B[0][1] + A[0][1]*B[1][1])%1000000007
    mat10 = (A[1][0]*B[0][0] + A[1][1]*B[1][0])%1000000007
    mat11 = (A[1][0]*B[0][1] + A[1][1]*B[1][1])%1000000007
    result = [[mat00, mat01],
              [mat10, mat11]]

    return result

def square_matrix(arr, n):
    result = [[1,0], [0,1]] # index 행렬
    while n >= 1:
        if n%2:
            result = multiple_matrix_2(result, arr)
        n //= 2
        arr = multiple_matrix_2(arr, arr)
    return result

def fibo(n):
    arr = [[1,1], [1,0]]
    square = square_matrix(arr, n)
    return square[0][1]


n = int(sys.stdin.readline())
print(fibo(n))