#11723 집합
import sys
input = sys.stdin.readline

M = int(input())
S = 0
for _ in range(M):
    order= list(input().strip().split())
    if order[0] == 'add':
        S |= (1<<int(order[1]))
    elif order[0] == 'remove':
        S -= S&(1<<int(order[1]))
    elif order[0] == 'check':
        if S & (1<<int(order[1])):
            print(1)
        else:
            print(0)
    elif order[0] == 'toggle':
        if S & (1<<int(order[1])):
            S &= (0<<int(order[1]))
        else:
            S |= (1<<int(order[1]))
    elif order[0] == 'all':
        # for i in range(1,21):
        #     S |= (1<<i)
        S =2097150
    elif order == 'empty':
        S = 0