# 11726 2xn 타일링
import sys
input = sys.stdin.readline


def solution():
    N = int(input())
    dp = [1] * (N+1)
    for i in range(2, N+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 10_007
    print(dp[N])

if __name__ == "__main__":
    solution()