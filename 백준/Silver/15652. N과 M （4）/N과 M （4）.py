import sys

def permutation(arr,start, n, m):
    if len(arr) == m:
        print(*arr)
        return

    for i in range(start, n+1):
        permutation(arr+[i], i, n, m)

N, M = map(int, sys.stdin.readline().strip().split())
lst = []
permutation(lst, 1, N, M)