import sys
input = sys.stdin.readline

k = int(input())
x, y = map(int, input().strip().split())
if k == 1:
    tile = [[1,1], [1,1]]
    n =2
    tile[n-y][x-1] = -1
else:
    tile = [[4,4,5,5],[4,3,3,5],[1,3,3,2],[1,1,2,2]]

    n =4
    if tile[n-y][x-1] == 1:
        tile[2][1] = 1
    elif tile[n-y][x-1] == 2:
        tile[2][2] = 2
    elif tile[n-y][x-1] == 4:
        tile[1][1] = 4
    elif tile[n-y][x-1] == 5:
        tile[1][2] = 5
    tile[n-y][x-1] = -1

for i in range(n):
    print(*tile[i])