M = int(input())
N = int(input())

def isPrime(n):                         # 소수확인
    if n >1:
        for num in range(2, n):
            if n % num == 0:
                return 0
        return 1
        

        
count = 0
min = 10001
prime = []
for num in range(M, N+1):       
    if isPrime(num):            # 소수면
        count += num            # 합 구하고
        if num < min:           # 최솟값 확인
            min = num
if count == 0:                  # 소수가 없으면 -1
    print(-1)
else:
    print(f'{count}\n{min}')