import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * 1001
inc = [1] * 1001
A = list(map(int, input().strip().split()))

if N >= 1:
    dp[0] = 1
    inc[0] = 1
if N >= 2:
    dp[1] = 2 if A[1] > A[0] else 1
    inc[1] = 2 if A[1] > A[0] else 1
if N >= 3:
    for i in range(2, N):
        for j in range(i):
            if A[i] > A[j]:
                inc[i] = max(inc[i], inc[j] + 1)
        dp[i] = max(inc[i], dp[i-1])
        
print(dp[N-1])