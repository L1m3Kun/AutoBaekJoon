# 2294 동전 2
import sys
input = sys.stdin.readline


def solution():
    N, K = map(int, input().split())
    coins = set([int(input()) for _ in range(N)])
    dp = [100_001] * (K+1)
    dp[0] = 0

    for coin in coins:
        for i in range(K+1):
            if dp[i] != 100_001:
                cnt = 1
                while i + coin*cnt <= K:
                    dp[i+coin*cnt] = min(dp[i+coin*cnt], dp[i]+cnt)
                    cnt += 1     
            if coin + i >K:
                break

    if dp[K] == 100_001:
        print(-1)
    else:
        print(dp[K])

if __name__ == "__main__":
    solution()