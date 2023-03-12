import sys
input = sys.stdin.readline

p = [list(map(int, input().strip().split())) for _ in range(3)]

res = (p[1][0]-p[0][0])*(p[2][1]-p[0][1]) - (p[1][1] - p[0][1])*(p[2][0]-p[0][0])
if res < 0:
    print(-1)
elif res > 0:
    print(1)
else:
    print(0)
