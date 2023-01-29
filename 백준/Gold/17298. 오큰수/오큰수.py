# import sys
#
# n = int(sys.stdin.readline())
# numbers = list(map(int, sys.stdin.readline().split()))
#
# bigger = [-1] * n
# for i in range(n):
#     for j in range(i+1, n):
#         if numbers[i] < numbers[j]:
#             bigger[i] = numbers[j]
#             break
#
# print(*bigger)

import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
ans = [-1] * n
count = []

for i in range(n):
    while count and numbers[count[-1]] < numbers[i]:
    # while "list" : "list" 안에 원소가 있으면 True (while문은 참이면 반복문 시행, 거짓이면 중단)
    # 0. i가 0일 때 count 안에 원소가 없기에 반복문은 시행 X
    # 0. count의 원소가 없는 경우 while문 자체에 진입이 안되기에 후발조건인 count[-1]에 관한 오류 X
    # 1. i = i, while문 시행 >> numbers[count[-1]] == numbers[0]
    # 2. ~ n-2. 은 위와 같음
    # n-1. count[-1] = n-1이기에 numbers[count[-1]] == numbers[i], 조건문 시행 X
        ans[count.pop()] = numbers[i]
        # 1. numbers[0] < numbers[i]인 경우에 ans[0]을 numbers[1]로 변경, count의 원소를 지움
        #    조건을 만족시키지 못하는 경우는 통과
        #    조건을 만족시키는 시점부터 반복해서 count의 원소를 지우고 이전 ans 값을 만족하는 numbers의 값으로 변경
    count.append(i)
    # 0. ~ n-1. 반복문의 시행과 관련 없이 count에 i를 원소로 append 시킴
    #           위의 조건을 만족시키지 못하는 경우 count의 길이가 증가

print(*ans)
