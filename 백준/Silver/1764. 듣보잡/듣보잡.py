import sys

N, M = map(int, sys.stdin.readline().strip().split())
no_seen = set(sys.stdin.readline().strip() for _ in range(N))
no_heard = set(sys.stdin.readline().strip() for _ in range(M))

cnt = 0
result = []
for s in no_seen:
    if s in no_heard:
       cnt += 1
       result.append(s)
print(cnt, *sorted(result), sep = "\n")
