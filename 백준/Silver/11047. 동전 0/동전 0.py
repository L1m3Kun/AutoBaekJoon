import sys

N, K = map(int, sys.stdin.readline().strip().split())

coin_lst = [int(sys.stdin.readline().strip()) for _ in range(N)]
coin_lst.sort(reverse=1)
cnt = 0
for coin in coin_lst:
    if K >= coin:
        cnt += K // coin
        K %= coin
    if K == 0:
        break
print(cnt)
