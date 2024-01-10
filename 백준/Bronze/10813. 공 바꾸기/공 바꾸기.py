import sys
input = sys.stdin.readline


def solution(n:int, m:int) -> list:
    basket = [i for i in range(n+1)]
    for _ in range(m):
        i, j = map(int, input().split())
        basket[i], basket[j] = basket[j], basket[i]  
        
    return basket[1:]


if __name__ == "__main__":
    n,m = map(int, input().split())
    
    
    print(*solution(n,m))