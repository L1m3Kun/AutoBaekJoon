import sys


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
try:
    print(*bubble_sort(arr, N, k))
except:
    print(bubble_sort(arr, N, k))