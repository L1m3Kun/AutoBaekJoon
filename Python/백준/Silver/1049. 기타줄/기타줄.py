# 1049 기타줄
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

min_six, min_one = 10001, 10001

for _ in range(M):
    six, one = map(int, input().split())

    min_six = min(six, min_six)
    min_one = min(one, min_one)
    
if min_one*6 < min_six:
    print(N * min_one)
else:
    cost = 0
    while N >= 6:
        cost += min_six
        N -= 6
        
    if min_one * N < min_six:
        print(cost+min_one*N)
    else:
        print(cost+min_six)
            