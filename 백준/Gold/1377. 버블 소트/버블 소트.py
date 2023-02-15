import sys

N = int(sys.stdin.readline())
arr = list((int(sys.stdin.readline().strip()), i) for i in range(N))
lst = []
arr2 = sorted(arr)
max_index = 0
for i in range(N):
    lst.append(arr2[i][1] - arr[i][1])
print(max(lst) +1)