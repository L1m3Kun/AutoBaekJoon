import sys

def fib(n, c):
    if n ==1 or n ==2:
        c += 1
        return 1
    else:
        c += 1
        return fib(n - 1, c) + fib(n - 2, c)

def fibonacci(n,c):
    arr = [0]*(n+1)
    if n ==1 or n ==2:
        c += 1
        arr[n] = 1
    else:
        for i in range(3, n+1):
            c += 1
            arr[i] = arr[i-1] + arr[i-2]
    return c

n = int(sys.stdin.readline())
count = cnt = 0
fib(n, count)
fibonacci(n, cnt)
print(fib(n, count), fibonacci(n, cnt))



