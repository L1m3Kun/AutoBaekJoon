import sys


def bubble_sort(lst, num, cnt):
    count = 0
    for last in range(num-1, 0, -1):
        for idx in range(last):
            if lst[idx] > lst[idx+1]:
                count += 1
                lst[idx], lst[idx+1] = lst[idx+1], lst[idx]
                if count == cnt:
                    return arr
    return -1


N, k = map(int, sys.stdin.readline().strip().split())
arr = list(map(int, sys.stdin.readline().strip().split()))

result = bubble_sort(arr, N, k)
if result == -1:
    print(result)
else:
    print(*result)
