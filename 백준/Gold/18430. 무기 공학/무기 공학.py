# 18430 무기 공학
import sys
input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    log = [list(map(int, input().split())) for _ in range(N)]

    bumerang = [(0,-1,1,0), (-1,0,0,-1), (-1,0,0,1), (1,0,0,1)]

    if N < 2 or M < 2:
        print(0)
        return

    visited = [[0] * M for _ in range(N)]

    def bt(idx, strength, maxv):
        if idx == N*M:
            maxv = max(maxv, strength)
            return maxv
        
    
        i,j = idx // M, idx % M
        if not visited[i][j]:

            for ly,lx, ry,rx in bumerang:
                ly+= i
                lx+= j
                ry+= i
                rx+= j
                if (
                    0 <= ly < N 
                    and 0 <= ry < N 
                    and 0 <= lx < M 
                    and 0 <= rx < M 
                    and not visited[ly][lx] 
                    and not visited[ry][rx]
                    ):
                    visited[ly][lx] = visited[i][j] =  visited[ry][rx] = 1
                    maxv = max(maxv, bt(idx+1, strength+log[i][j] * 2+log[ly][lx]+log[ry][rx], maxv))
                    visited[ly][lx] = visited[i][j] =  visited[ry][rx] = 0
        
        maxv = max(maxv, bt(idx+1, strength, maxv))
        return maxv 
    
    print(bt(0, 0, 0))
    return


if __name__ == "__main__":
    main()