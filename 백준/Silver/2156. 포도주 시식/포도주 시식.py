import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
dp = [0] * (N + 1)
if N >= 1:
    dp[0] = arr[0]
if N >= 2:
    dp[1] = arr[1] + arr[0]
if N >= 3:
    dp[2] = max(arr[2]+arr[1], arr[2]+arr[0], arr[1]+arr[0])
if N >= 4:
    dp[3] = max(arr[3]+arr[2]+dp[0], arr[3]+arr[1]+dp[0], arr[2]+arr[1])
if N >= 5:
    for i in range(4, N):
        dp[i] = max(arr[i]+arr[i-1] + dp[i-3], arr[i-1]+arr[i-2]+dp[i-4], arr[i] + dp[i-2])
print(dp[N-1])