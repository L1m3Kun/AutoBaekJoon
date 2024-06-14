# 1669 멍멍이 쓰다듬기
import sys
input = sys.stdin.readline

X, Y = map(int, input().split())

target= Y-X

if target in (0, 1, 2, 3):
    print(target)
else:
    day = int(target ** (1/2) )
    if target == day ** 2:
        print(day+day-1)
    elif day * (day+1) >= target :
        print(day+day)
    # elif (day + 1) ** 2 >= target:
    else:
        print(day+day+1)
