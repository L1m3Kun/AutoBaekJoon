import sys
input = sys.stdin.readline

def factorial(N):
    if N == 0:
        return 1
    if N == 1:
        return 1
    if N == 2:
        return 2
    return N * factorial(N-1)

N = int(input())

print(factorial(N))