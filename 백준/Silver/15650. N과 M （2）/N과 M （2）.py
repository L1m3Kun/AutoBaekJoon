import sys

def combination(arr,start, n, m):
    if len(arr) == m:
        print(*arr)
        return
    for i in range(start, n+1):
        if i not in arr:
            arr.append(i)
            combination(arr,i, n, m)
            arr.pop()
            
N, M = map(int, sys.stdin.readline().strip().split())
lst = list( range(1, N+1))

lst = []
combination(lst,1, N, M)