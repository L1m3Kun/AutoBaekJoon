# 2294 동전 2
import sys
input = sys.stdin.readline


def solution():
    N, K = map(int, input().split())
    coins = set([int(input()) for _ in range(N)])
    dp = [100_001] * (K+1)
    dp[0] = 0

    for i in range(K+1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i-coin]+1, dp[i])    

    if dp[K] == 100_001:
        print(-1)
    else:
        print(dp[K])

if __name__ == "__main__":
    solution()