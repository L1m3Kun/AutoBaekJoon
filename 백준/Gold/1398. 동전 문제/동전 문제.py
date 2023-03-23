import sys
input = sys.stdin.readline

def bf_part(price):
    coin = [10 ,1]
    ram = price // 25

    min_val = price
    for i in range(ram+1):
        num = str(price - 25 * i)
        if len(num) ==2:
            ans = int(num[0])+ int(num[1]) + i
        else:
            ans = int(num) + i
        if min_val > ans:
            min_val = ans 
    return min_val

def dp_part(price):
    n = len(price)
    if n == 1:
        print(int(*price))
        return 
    ans = 0
    if n%2:
        price = ['0'] + price
    # for i in range(0, n//2+1, 2):
    #     # dp[i]=bf_part(int(price[n-2*i-2]+price[n-2*i-1]))
    #     ans+=bf_part(int(price[i]+price[i+1]))
    for i in range(0,len(price),2):
        # dp[i]=bf_part(int(price[n-2*i-2]+price[n-2*i-1]))
        ans+=bf_part(int(price[i]+price[i+1]))
    # print(dp)
    # print(sum(dp))
    print(ans)
    return

for _ in range(int(input())):
    price = list(input().strip())

    dp_part(price)