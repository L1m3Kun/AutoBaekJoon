def fibo(n):
    if n == 0 :
        return 0            # 0번째 피보나치 수는 0
    elif n == 1:
        return 1            # 1번째 피보나치 수는 1
    return fibo(n-2)+ fibo(n-1) # n 번째 피보나치 수는  n-2 + n-1

n = int(input())
print(fibo(n))
