# 1003 피보나치 함수
import sys
input = sys.stdin.readline


def solution(N:int) -> list:
    dp = [[0, 0] for _ in range(N+1)]
    dp[0] = [1, 0]
    if not N:
        return dp[0]
    dp[1] = [0, 1]
    for i in range(2, N+1):
        dp[i][0] = dp[i-1][0] + dp[i-2][0]
        dp[i][1] = dp[i-1][1] + dp[i-2][1]
    
    return dp[-1]


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        print(*solution(int(input())))