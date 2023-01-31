import sys
from collections import deque

N, k = deque(map(int,sys.stdin.readline().strip().split()))
yoseputh = deque(range(1, N+1))
result = []
count = 1
while True:
    if len(result) != N:
        k_idx = yoseputh.popleft()
        if count % k == 0:
            result.append(k_idx)
        else:
            yoseputh.append(k_idx)
        count += 1
    else:
        break
# print(result)
print('<', end='')
print(*result, end='',sep= ', ')
print('>')