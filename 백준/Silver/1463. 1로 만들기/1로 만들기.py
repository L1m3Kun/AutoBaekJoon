import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (10**6+1)
if N >= 1:
    dp[0] = 0
if N >= 2:
    dp[1] = 1
if N >= 3:
    dp[2] = 1
if N >= 4:
    for i in range(4, N+1):
        if not i % 3 and not i % 2:
            dp[i-1] = 1 + min(dp[i-2], dp[(i-2)//3], dp[(i-2)//2])
        elif not i % 3:
            dp[i-1] = 1 + min(dp[i-2], dp[(i-2)//3])
        elif not i % 2:
            dp[i-1] = 1 + min(dp[i-2], dp[(i-2)//2])
        else:
            dp[i-1] = 1 + dp[i-2]
    
print(dp[N-1])    