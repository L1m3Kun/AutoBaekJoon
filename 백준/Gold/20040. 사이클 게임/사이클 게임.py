# 20040 사이클 게임
import sys
input = sys.stdin.readline


def find(x:int):
    # recursionError
    # if x == spots[x]:
    #     return spots[x]
    # spots[x] = find(spots[x])
    tmp = x
    while tmp != spots[tmp]:
        tmp = spots[tmp]
    spots[x] = spots[tmp]
    return spots[x]


def union(num1:int, num2:int):
    f1 = find(num1)
    f2 = find(num2)
    if f1 != f2:
        spots[f2] = f1
        return 0
    return 1



def solution(N:int, M:int) -> int:
    for _ in range(2):
        s, e = map(int, input().split())
        union(s, e)
    for turn in range(3, M+1):
        s, e = map(int, input().split())
        if union(s, e):
            return turn
    return 0


if __name__ == "__main__":
    N, M = map(int, input().split())
    spots = [i for i in range(N)] 
    print(solution(N, M))