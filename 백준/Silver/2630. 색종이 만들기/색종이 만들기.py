import sys
input = sys.stdin.readline

def check(paper):
    res = 0
    for i in range(len(paper)):
        res += sum(paper[i])
    return res

def solution(paper):
    global blue, white
    if len(paper) == 1:
        if paper[0][0] == 1:
            blue += 1
        else:
            white += 1
        return
    if check(paper) == len(paper)**2:
        blue += 1
        return
    elif check(paper) == 0:
        white += 1
        return
    else:
        n = len(paper)
        half = n//2
        tmp = [[0] * (half) for _ in range(half)]
        for i in range(half):
            for j in range(half):
                tmp[i][j] = paper[i][j]     
        solution(tmp)

        for i in range(half):
            for j in range(half, n):
                tmp[i][j-half] = paper[i][j]     
        solution(tmp)

        for i in range(half, n):
            for j in range(half):
                tmp[i-half][j] = paper[i][j]     
        solution(tmp)
        
        for i in range(half, n):
            for j in range(half, n):
                tmp[i-half][j-half] = paper[i][j]     
        solution(tmp)
        return 
        




N = int(input())
paper = [list(map(int, input().strip().split())) for _ in range(N)]
white = blue = 0
solution(paper)
print(white, blue, sep='\n')
    