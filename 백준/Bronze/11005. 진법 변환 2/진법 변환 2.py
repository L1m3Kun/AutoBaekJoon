# 11005 진법 변환 2
import sys
input = sys.stdin.readline


def solution():
    N, B = map(int, input().split())
    s = ""
    while N > 0:
        s += str(N%B) if N%B < 10 else chr(N%B+55)
        N //= B
    print(s[::-1])
if __name__ == "__main__":
    solution()