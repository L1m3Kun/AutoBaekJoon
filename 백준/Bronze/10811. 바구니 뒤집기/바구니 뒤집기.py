import sys
input = sys.stdin.readline


def solution(n:int, m:int) -> list:
    basket = [i for i in range(1,n+1)]
    for _ in range(m):
        i, j = map(int, input().split())
        tmp = basket[i-1:j].copy()
        for k in range(i-1, j):
            basket[k] = tmp[j-k-1]            
        
    return basket


if __name__ == "__main__":
    n,m = map(int, input().split())
    
    
    print(*solution(n,m))