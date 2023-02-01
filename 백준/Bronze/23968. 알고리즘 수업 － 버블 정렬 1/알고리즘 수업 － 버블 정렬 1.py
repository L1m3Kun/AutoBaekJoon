import sys

'''
Bubble Sort 
바로 오른쪽 자리와 비교하여 작은 값(내림차순의 경우 큰 값)을 만났을 때 자리 바꾸기

try: except: 활용 최소화
if result == -1 이면 으로 바꿈 (다른사람 코드 참조)
'''


def bubble_sort(lst, last, num):
    count = 0
    for n in range(last-1, 0, -1):
        for idx in range(n):
            if lst[idx] > lst[idx + 1]:
                count += 1
                lst[idx], lst[idx + 1] = lst[idx + 1], lst[idx]
                if count == num:
                    return lst[idx], lst[idx+1]
    return -1


N, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().strip().split()))
result = bubble_sort(arr, N, k)
if result == -1:
    print(result)
else:
    print(*result)

# try:
#     print(*bubble_sort(arr, N, k))
# except:
#     print(bubble_sort(arr, N, k))

