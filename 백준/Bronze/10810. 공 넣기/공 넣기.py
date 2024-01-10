
import sys
input = sys.stdin.readline


def solution(n:int, m:int) -> list:
    basket = [0] * (n+1)
    for _ in range(m):
        i, j, k = map(int, input().split())
        for idx in range(i, j+1):
            basket[idx] = k
    return basket[1:]


if __name__ == "__main__":
    n,m = map(int, input().split())
    
    
    print(*solution(n,m))