import sys
input = sys.stdin.readline

N = int(input())
dp = [[0] * 10 for _ in range(N+1)]
if N >= 1:
    for i in range(1,10):
        dp[0][i] = 1
if N >= 2:
    for i in range(1, N):
        for j in range(10):
            left = dp[i-1][j-1] if j-1 >=0 else 0
            right = dp[i-1][j+1] if j+1 <=9 else 0
            dp[i][j] = left + right
# print(dp[:N])
if N == 1:
    print(9)
else:
    print(sum(dp[N-1]) % 10**9)