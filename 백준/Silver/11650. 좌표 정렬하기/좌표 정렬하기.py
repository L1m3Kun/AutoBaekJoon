import sys

N = int(sys.stdin.readline())
matrix_list = []
for _ in range(N):
    matrix_list.append(list(map(int, sys.stdin.readline().strip().split())))

for idx in sorted(matrix_list):
    print(*idx)