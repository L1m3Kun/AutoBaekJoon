T = int(input())
def prime(n):
    if n == 2:
        return True
    else:
        for idx in range(2,int(n **(1/2)) + 1):
            if n % idx ==0:
                return False
        else:
            return True

for test_case in range(T):
    n = int(input())
    less_half = more_half = n // 2
    while True:
        if prime(less_half) and prime(more_half):
            print(less_half, more_half)        
            break
        elif less_half == 1:
            break
        elif more_half == n:
            break
        less_half -= 1
        more_half += 1
    

''' 시간단축
    n = int(input())
    prime = [False, False] + [True] * (n - 1)
    for idx in range(2,n):
        if prime[idx]:
            for non_prime in range(idx * 2, n + 1, idx):
                prime[non_prime] = False
    
    for idx in range(n//2,1,-1):
        if prime[idx]:
            if prime[n-idx]:
                num  = idx
                break
    if num <= n-num:
        print(num, n-num)
    else:
        print(n - num, num)
'''