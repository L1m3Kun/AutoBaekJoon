# 2869 달팽이는 올라가고 싶다
import math
input = __import__("sys").stdin.readline


def solution(A:int, B:int, V:int) -> int:
    return math.ceil((V-A)/(A-B)) +1


if __name__ == "__main__":
    print(solution(*list(map(int, input().split()))))