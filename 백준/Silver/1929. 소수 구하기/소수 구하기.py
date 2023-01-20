import sys
'''
def Prime_lst(m,n):
    for num in range(m,n+1):
        if num > 1:    
            for i in range(2,int(num**0.5)+1):          # 제곱근 n까지 확인
                if num % i == 0:                            
                    break
            else:
                print(num)
'''
# 시간 단축

# 에라토스테네스의 채
def Prime_lst(m, n):
    prime_lst = [False, False] + [True] * (n-1)
    for num in range(2, n+1):
        if prime_lst:
            for idx in range(num*2, n+1, num):
                prime_lst[idx] = False
    for prime in range(m, len(prime_lst)):
        if prime_lst[prime]:
            print(prime)

M,N = map(int, sys.stdin.readline().strip().split())

Prime_lst(M,N)

