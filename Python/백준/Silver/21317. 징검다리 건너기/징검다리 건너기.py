# 21317 징검다리 건너기
import sys
input = sys.stdin.readline

n = int(input().strip())
energy = tuple(tuple(map(int, input().split())) for _ in range(n-1))
k = int(input())

dp = [[100000, 100000] for _ in range(n)]
dp[0] = [0,0]
for i in range(n):
    if (n-1-i) >= 1:
        dp[i+1][0] = min(dp[i+1][0], dp[i][0]+energy[i][0])
        dp[i+1][1] = min(dp[i+1][1], dp[i][1]+energy[i][0])
    if (n-1-i) >= 2:
        dp[i+2][0] = min(dp[i+2][0], dp[i][0]+energy[i][1])
        dp[i+2][1] = min(dp[i+2][1], dp[i][1]+energy[i][1])
    if (n-1-i) >= 3:
        dp[i+3][1] = min(dp[i+3][1], dp[i][0]+k)
    # print(dp)
print(min(dp[-1]))

