import sys
import math

Min, Max = map(int, sys.stdin.readline().strip().split())

arr = [1] * (Max - Min + 1)
for i in range(2, int(Max ** (0.5) + 1)):
    for j in range(math.ceil(Min/i**2) * i**2, Max+1, i**2):
        arr[j - Min] = 0

print(sum(arr))