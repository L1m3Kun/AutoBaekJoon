import sys
input = sys.stdin.readline


def f(num):
    total = 1
    for i in range(1, num+1):
         total *= i
    return total


def solution():
    r, n = map(int, input().split())
    print(f(n)//(f(r) * f(n-r)))


if __name__ == "__main__":
    for _ in range(int(input())):
        solution()