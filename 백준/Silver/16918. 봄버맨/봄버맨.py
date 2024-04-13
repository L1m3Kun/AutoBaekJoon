# 16918 봄버맨
import sys
input = sys.stdin.readline


def main():
    R, C, N = map(int, input().split())
    field = [list(input().strip()) for _ in range(R)]

    def fill_bombs(fields, bombs, now):
        bombs[now+3] = set()
        for i in range(R):
            for j in range(C):
                if fields[i][j] == ".":
                    bombs[now+3].add((i,j))
                    fields[i][j] = "O"
        return
    

    def boom(fields, bombs, now):
        if now not in bombs:
            return 
        for i,j in bombs[now]:
            for di, dj in [(0,0), (0,1), (0,-1), (1,0), (-1,0)]:
                ni,nj = i+di, j+dj
                if 0 <= ni < R and 0 <= nj < C:
                    fields[ni][nj] = "."
                    bombs[now+2].discard((ni,nj))
        return


    bombs = {}
    bombs[3] = set()
    for i in range(R):
        for j in range(C):
            if field[i][j] == "O":
                bombs[3].add((i,j))
        
    
    
    t = 2
    while t <= N:
        if t % 2:
            boom(field, bombs, t)
        else:
            fill_bombs(field, bombs, t)
        t += 1
    
    for i in range(R):
        print("".join(field[i]))
    

    return


if __name__ == "__main__":
    main()
    

