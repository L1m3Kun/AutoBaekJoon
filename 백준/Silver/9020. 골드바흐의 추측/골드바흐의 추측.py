T = int(input())
for test_case in range(T):
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
