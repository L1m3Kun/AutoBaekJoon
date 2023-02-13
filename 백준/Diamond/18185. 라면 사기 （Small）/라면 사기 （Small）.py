import sys
N = int(sys.stdin.readline().strip())
buy_list = list(map(int, sys.stdin.readline().strip().split()))
i = 0
cost = 0
while i < N:
    if buy_list[i]:
        if i < N-2 and buy_list[i]>0 and buy_list[i+1]>0 and buy_list[i+2]>0 and buy_list[i+1]<=buy_list[i+2]:
            mini = min(buy_list[i], buy_list[i + 1], buy_list[i + 2])
            cost += 7 * mini
            buy_list[i] -= mini
            buy_list[i + 1] -= mini
            buy_list[i + 2] -= mini
            if buy_list[i]:
                continue
        elif i < N-2 and buy_list[i]>0 and buy_list[i+1]>0 and buy_list[i+2]>0:
            # mini = min(buy_list[i], buy_list[i + 1])
            cost += 5
            buy_list[i] -= 1
            buy_list[i + 1] -=1
            if buy_list[i]:
                continue
        if i < N-1 and buy_list[i]>0 and buy_list[i+1]>0:
            mini = min(buy_list[i], buy_list[i+1])
            cost += 5 * mini
            buy_list[i] -= mini
            buy_list[i + 1] -= mini
            if buy_list[i]:
                continue
        else:
            cost += 3 *buy_list[i]
        i += 1
    else:
        i += 1
print(cost)