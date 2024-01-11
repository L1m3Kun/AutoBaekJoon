# 1932 정수 삼각형
import sys
input = sys.stdin.readline


def solution():
    triangle = [[0] * n for _ in range(n)]
    for i in range(n):
        tmp = list(map(int, input().split()))
        for j in range(i+1):
            triangle[i][j] = tmp[j]
    for i in range(1, n):
        for j in range(i+1):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == i:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])

        
    return max(triangle[-1])


if __name__ == "__main__":
    n = int(input())
    
    print(solution())


