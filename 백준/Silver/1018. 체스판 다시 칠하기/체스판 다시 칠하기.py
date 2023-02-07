import sys

N, M = map(int, sys.stdin.readline().strip().split())
rect = [list(sys.stdin.readline().strip()) for _ in range(N)]
chess1 = []
# print(rect)
min_paint = 64
# chess2 = []
for i in range(8):
    if i % 2:
        chess1.append(['B', 'W', 'B', 'W','B','W','B','W'])
        # chess2.append(['w', 'b', 'w', 'b', 'w', 'b', 'w', 'b'])
    else:
        chess1.append(['W' ,'B', 'W', 'B', 'W','B','W','B'])
        # chess2.append(['b', 'w', 'b', 'w','b','w','b','w'])
# print(chess1)
for i in range(N-7):
    for j in range(M-7):
        count_b = count_w = 0
        for k in range(8):
            for l in range(8):
                if rect[i+k][j+l] != chess1[k][l]:
                    # print(1, end=" ")
                    count_b += 1
                else:
                    # print(0, end=" ")
                    count_w += 1
        # print(count_w, count_b)
        if min_paint > count_b:
            min_paint = count_b
        if min_paint > count_w:
            min_paint = count_w
print(min_paint)