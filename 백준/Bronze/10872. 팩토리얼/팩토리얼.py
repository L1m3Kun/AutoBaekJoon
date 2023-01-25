def factorial(n):
    if n == 1 or n == 0:            # 재귀 탈출
        return 1
    return factorial(n-1) * n       # 재귀 호출 n을 1씩 줄이면서

N = int(input())
print(factorial(N))