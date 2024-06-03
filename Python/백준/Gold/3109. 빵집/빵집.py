# 3109 빵집
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
ground = tuple(input().strip() for _ in range(R))


def makePipeLine(row):
    stack = [(row,0)] # i, j, cnt

    while stack:
        i, j = stack.pop()
        visited[i][j] = 1
        if j == C-1:
            return 1
        

        for di in range(1, -2, -1):
            ni,nj = i+di, j+1
            if 0 <=ni < R and nj < C:
                if ground[ni][nj] != 'x' and not visited[ni][nj]:
                    stack.append((ni,nj))
    
    return 0

ans = 0
visited = [[0] * C for _ in range(R)]

for i in range(R):
    maxv = 0
    if ground[i][0] != "x":
        visited[i][0] = 1
        ans += makePipeLine(i)
# [print(visited[k]) for k in range(R)]
print(ans)  