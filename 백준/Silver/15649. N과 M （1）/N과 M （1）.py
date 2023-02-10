import sys

def permutation(arr, n, m):
    if len(arr) == m:
        print(*arr)
        return
    else:
        for i in range(1, n+1):
            if i not in arr:
                arr.append(i)
                permutation(arr, n, m)
                arr.pop()

N, M = map(int, sys.stdin.readline().strip().split())
lst = []
permutation(lst, N, M)