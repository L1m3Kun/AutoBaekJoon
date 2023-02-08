import sys
# 입력
N = int(sys.stdin.readline())
sang = {}
for m in list(map(int, sys.stdin.readline().strip().split())):
    if m not in sang.keys():
        sang[m] = 1
    else:
        sang[m] += 1
M = int(sys.stdin.readline())
for q in list(map(int, sys.stdin.readline().strip().split())):
    if q in sang.keys():
        print(sang[q], end=" ")
    else:
        print(0, end=" ")
