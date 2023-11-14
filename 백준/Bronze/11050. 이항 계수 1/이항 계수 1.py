# 11050 이항 계수 1
import sys

input = sys.stdin.readline


def factorial(N: int) -> list[int]:
    ft = [0] * (N + 1)
    ft[0], ft[1] = 1, 1
    for i in range(2, N + 1):
        ft[i] = i * ft[i - 1]
    return ft


def solution(N: int, K: int) -> int:
    f = factorial(N)
    return f[N] // (f[K] * f[N - K])


if __name__ == "__main__":
    N, K = map(int, input().split())
    print(solution(N, K))
