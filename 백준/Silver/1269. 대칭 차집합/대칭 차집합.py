import sys


N, M = map(int, sys.stdin.readline().strip().split())
A = set(map(int, sys.stdin.readline().strip().split()))
B = set(map(int, sys.stdin.readline().strip().split()))
result = set()
result.update(A, B)
for i in B:
    if i in A:
        result.discard(i)
print(len(result))

