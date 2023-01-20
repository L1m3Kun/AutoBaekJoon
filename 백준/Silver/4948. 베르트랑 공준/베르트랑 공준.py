def bertrang_theory(n):
    prime_lst = [0,0] + [1] * (2 * n - 1)    
    for num in range(2, 2*n+1):                           # n보다 크고  2n보다 작거나 같은
        if prime_lst[num]:
            for idx in range(num * 2, 2 * n + 1, num):
                prime_lst[idx] = 0                      # 소수 저장
    return sum(prime_lst[n+1:])
while True:
    n = int(input())
    if n == 0:
        break
    print(bertrang_theory(n))