import sys


N, M = map(int, sys.stdin.readline().strip().split())
A = set(map(int, sys.stdin.readline().strip().split()))
for i in set(map(int, sys.stdin.readline().strip().split())):
    if i not in A:
        A.add(i)
    else:
        A.discard(i)
print(len(A))