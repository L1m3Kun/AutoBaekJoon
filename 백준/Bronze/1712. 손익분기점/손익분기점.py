import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())
if C != B:
    n = A/(C-B)
    if n >= 0:
        print(int(n)+1)
    else:
        print(-1)
else:
    print(-1)
