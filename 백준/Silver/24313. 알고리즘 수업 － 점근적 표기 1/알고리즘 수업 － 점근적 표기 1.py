# 24313 알고리즘 수업 - 점근적 표기 1
import sys
input = sys.stdin.readline


def solution():
    a1, a0 = map(int, input().split())
    c = int(input())
    n0 = int(input())
    if n0 * c >= a1*n0 + a0 and a1 <= c:
        print(1)
    else:
        print(0)


if __name__ == "__main__":
    solution()