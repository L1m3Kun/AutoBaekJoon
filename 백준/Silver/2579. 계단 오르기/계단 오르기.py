import sys
input = sys.stdin.readline

N = int(input())
stairs = [int(input()) for _ in range(N)]
# print(stairs)
dp = [0] * 301
if N >= 1:
    dp[0] = stairs[0]
if N >= 2:
    dp[1] = stairs[1] + stairs[0]
if N >= 3:
    dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])
if N >= 4:
    for i in range(4, N+1):
        dp[i-1] = stairs[i-1] + max(dp[i-3], dp[i-4]+stairs[i-2])
print(dp[N-1])