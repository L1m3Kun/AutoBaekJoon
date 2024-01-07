# 1717 집합의 표현
import sys
input = sys.stdin.readline

def find(num:int)->int:
    if parent[num] == num:
        return num
    parent[num] = find(parent[num])
    return parent[num]


def union(num1:int, num2:int) -> None:
    x = find(num1)
    y = find(num2)
    if x != y:
        parent[y] = x
    return


def solution(n:int, m:int) -> None:
    for _ in range(m):
        order, a, b = map(int, input().split())
        if order:       # 같은 집합인가 확인
            if find(a) == find(b):
                print("yes")
            else:
                print("no")
        else:           # 합집합
            union(a, b)
    return


if __name__ == "__main__":
    # input
    n, m = map(int, input().split())
    parent = [i for i in range(n+1)]
    solution(n, m)