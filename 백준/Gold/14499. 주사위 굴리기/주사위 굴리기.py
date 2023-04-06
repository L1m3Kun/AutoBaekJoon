import sys
input = sys.stdin.readline


def game_start(i, j):
    top = 1
    # bottom = 5
    for now in range(K):
        request = orders[now]
        di, dj = move[request]
        ni, nj = i+di, j+dj
        if 0<=ni<N and 0<=nj<M:
            # 방향 = 1
            if request == 1:
                # print('->')
                tmp = row[0]
                for idx in range(2):
                    row[idx] = row[idx+1]
                row[2] = top
                col[1] = row[1]
                bottom = check_field(ni,nj, row[1])
            # 방향 = 2
            elif request == 2:
                # print('<-')
                pass
                tmp = row[2]
                for idx in range(2,0,-1):
                    row[idx] = row[idx-1]
                row[0] = top
                col[1] = row[1]
                bottom = check_field(ni,nj, row[1])
            # 방향 = 3
            elif request == 3:
                # print('A')
                pass
                tmp = col[2]
                for idx in range(2,0,-1):
                    col[idx] = col[idx-1]
                col[0] = top
                row[1] = col[1]
                bottom = check_field(ni,nj, col[1])
            # 방향 = 4
            elif request == 4:
                # print('V')
                pass
                tmp = col[0]
                for idx in range(2):
                    col[idx] = col[idx+1]
                col[2] = top
                row[1] = col[1]
                bottom = check_field(ni,nj, col[1])

            top = tmp
            i,j= ni, nj
            # dice[row[1]] = bottom
            # print('top=',top)
            # print('bottom =', row[1])
            # print('dice', dice)
            # print('dice idx')
            # print(*col, sep="\n")
            # print(*row)
            # print('field')
            # [print(field[a]) for a in range(N)]
            print(dice[top])
            # print('-------------')
    return

def check_field(x, y, bottom):
    # bottom = dice[k]
    tmp = field[x][y]
    if tmp:
        pass
        field[x][y] = 0
        dice[bottom] = tmp
        # return tmp
    else:
        pass
        field[x][y] = dice[bottom]
        # return 0
    return
        
        

# 지도 세로: N, 지도 가로:M, 주사위 처음 위치(세로:x,가로:y)
N, M, x, y, K = map(int, input().split())
field = []
for _ in range(N):
    field.append(list(map(int, input().split())))
orders = list(map(int, input().split()))
#  1: 동쪽, 2: 서쪽, 3: 북쪽, 4: 남쪽
move = [(0,0), (0,1), (0,-1), (-1, 0), (1,0)]
# 주사위 값 저장
dice = [0, 0, 0, 0, 0, 0, 0]
# 주사위 index
col = [2, 6, 5] # 가로
row = [4, 6, 3] # 세로
game_start(x, y)
