import sys

N = int(sys.stdin.readline().strip())
num = list(map(int, sys.stdin.readline().strip().split()))

prime = []

for number in num:
    if number > 1:
        count =0
        for less in range(2, number):   # 배수가 있는가 
            if number % less == 0:
                count = 1
        if count == 0:
            prime.append(number)        # 소수 모으기
print(len(prime))