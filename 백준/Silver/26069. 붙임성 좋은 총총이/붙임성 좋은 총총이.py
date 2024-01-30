# 26069 붙임성 좋은 총총이
import sys
input = sys.stdin.readline


def solution():
    N = int(input())
    dance = set(["ChongChong"])
    for _ in range(N):
        r1, r2 = input().strip().split()
        if r1 in dance or r2 in dance:
            dance.add(r1)
            dance.add(r2)
    print(len(dance))


if __name__ == "__main__":
    solution()