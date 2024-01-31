# 1629 곱셈
import sys
input = sys.stdin.readline


def solution():
    A, B, C = map(int, input().split())
    ans = 1
    while B > 0:
        if B % 2:
            ans *= A
            ans %= C
        B //=2
        A *= A
        A %= C
    print(ans)

if __name__ == "__main__":
    solution()