import sys

matrix_list = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(int(sys.stdin.readline()))]
matrix_list.sort(key=lambda x: (x[1], x[0]))
print("\n".join([(str(x[0])+" "+str(x[1])) for x in matrix_list]))