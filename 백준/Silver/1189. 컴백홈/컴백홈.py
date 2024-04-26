# 1189 컴백홈
import sys
# from collections import deque
input = sys.stdin.readline


def main():
    R, C, K = map(int, input().split())
    field = tuple(input().strip() for _ in range(R))
    
    def bfs():
        # que = deque([(R-1, 0, set([(R-1)*C]))])
        stack = [(R-1, 0, set([(R-1)*C]))]
        cnt = 0
        while stack:
            i, j, visited = stack.pop()
            if (i,j) == (0, C-1):
                if len(visited) == K:
                    # print(visited)
                    cnt += 1
                continue
            
            if len(visited) >= K:
                continue

            for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                ni, nj = di + i, dj + j
                if 0 <= ni < R and 0 <= nj < C:
                    if field[ni][nj] != "T" and (ni*C+nj) not in visited:
                        stack.append((ni,nj, visited.union(set([ni*C+nj]))))
        
        return cnt


    print(bfs())        

    return


if __name__ == "__main__":
    main()

