import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
rev_arr = arr[::-1]
inc = [1] * N
dec = [1] * N
dp = [0] * N
for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            inc[i] = max(inc[i], inc[j]+1)
        if rev_arr[i] > rev_arr[j]:
            dec[i] = max(dec[i], dec[j]+1)
max_val = 0
for i in range(N):
    max_val = max(max_val,inc[i] + dec[N-1-i] -1)

print(max_val)

