# 4779 칸토어 집합
import sys

input = sys.stdin.readline


def make_line(start: int, end: int) -> None:
    global lines
    if end - start <= 1:
        print("-", end="")
        return
    third = (end - start) // 3
    make_line(start, start + third)
    print(" " * third, end="")
    make_line(start + 2 * third, end)
    return


def solution(N: int) -> None:
    make_line(0, 3**N)
    print()
    return


if __name__ == "__main__":
    while True:
        s = input().strip()
        if not s:
            break
        N = int(s)
        solution(N)
