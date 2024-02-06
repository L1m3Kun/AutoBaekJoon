# 17143 낚시왕
import sys
input = sys.stdin.readline

def moving(R:int, C:int, M:int, ocean:list, sharks:list):
    tmp = [[0] * (C+1) for _ in range(R+1)]
    for i in range(1, M+1):
        if sharks[i] != 0:
            r, c, s, d, z = sharks[i]
            if s == 0:
                if tmp[r][c]:
                    if sharks[tmp[r][c]][4]<sharks[i][4]:
                        sharks[tmp[r][c]] = 0
                        tmp[r][c] = i
                    else:
                        sharks[i] = 0
                else:
                    tmp[r][c] = i

                continue
            if d == 1:
                if s > r-1:
                    k = s-r+1
                    dir = 1
                    while k > R-1:
                        k -= R-1
                        dir += 1
                    
                    if dir%2:
                        r = k+1
                        d = 2
                    else:
                        r = R-k
                else:
                    r -= s

            elif d == 2:
                if s > R-r:
                    k = s-(R-r)
                    dir = 1
                    while k > R-1:
                        k -= R-1
                        dir += 1
                    
                    if dir%2:
                        r = R-k
                        d = 1
                    else:
                        r = k+1
                        
                else:
                    r += s
                
                
            elif d == 3:
                if s > C-c:
                    k = s-(C-c)
                    dir = 1
                    while k > C-1:
                        k -= C-1
                        dir += 1
                    
                    if dir%2:
                        c = C-k
                        d = 4
                    else:
                        c = k+1
                        
                else:
                    c += s
            else:
                if s > c-1:
                    k = s-(c-1)
                    dir = 1
                    while k > C-1:
                        k -= C-1
                        dir += 1
                    
                    if dir%2:
                        c = k+1
                        d = 3
                    else:
                        c = C-k
                        
                else:
                    c -= s
            sharks[i] = (r, c, s, d, z)
            if tmp[r][c]:
                    if sharks[tmp[r][c]][4]<sharks[i][4]:
                        sharks[tmp[r][c]] = 0
                        tmp[r][c] = i
                    else:
                        sharks[i] = 0
            else:
                tmp[r][c] = i
    for ni in range(1, R+1):
        for nj in range(1, C+1):
            ocean[ni][nj] = tmp[ni][nj]
    return


def solution():
    for _ in range(M):
        # d 위 1, 아래 2, 오른쪽 3, 왼쪽 4
        sharks.append(tuple(map(int, input().split())))
    for i in range(1,M+1):
        r, c, s, d, z = sharks[i]
        ocean[r][c] = i
    shark_sizes = 0
    for turn in range(1,C+1):
        for i in range(1, R+1):
            if ocean[i][turn]:
                shark_sizes += sharks[ocean[i][turn]][4]
                sharks[ocean[i][turn]] = 0
                ocean[i][turn] = 0
                break
        moving(R, C, M, ocean, sharks)
    print(shark_sizes)


if __name__ == "__main__":
    R, C, M = map(int, input().split())
    ocean = [[0] * (C+1) for _ in range(R+1)]
    sharks = [0]
    solution()
