# 11660 구간 합 구하기 5
import sys
input = sys.stdin.readline


def solution():
    N, M = map(int, input().split())
    prefix_mat = [[0]*(N+1)]+[[0] + list(map(int, input().split())) for _ in range(N)]
    for i in range(1,N+1):
        for j in range(1,N+1):
            prefix_mat[i][j] += prefix_mat[i-1][j] + prefix_mat[i][j-1] - prefix_mat[i-1][j-1]
            

    for _ in range(M):
        x1, y1, x2, y2 = map(int, input().split())
        ans = prefix_mat[x2][y2]
        check = [0] * 2
        if x1:
            ans -= prefix_mat[x1-1][y2]
            check[0] = 1

        if y1:
            ans -= prefix_mat[x2][y1-1]
            check[1] = 1

        if check[0] and check[1]:
            ans += prefix_mat[x1-1][y1-1]

        print(ans)


if __name__ == "__main__":
    solution()
