# 16967 배열 복원하기
import sys
input = sys.stdin.readline


def main():
    H, W, X, Y = map(int, input().split())
    B = tuple(tuple(map(int, input().split())) for _ in range(H+X))
    A = [[0] * W for _ in range(H)]

    for i in range(H+X):
        for j in range(W+Y):
            if 0 <= i < H and 0 <= j < W:
                A[i][j] += B[i][j]
            
                if 0 <= i-X < H and 0 <= j-Y < W:
                    A[i][j] -= A[i-X][j-Y]
            
    
    for i in range(H):
        print(*A[i])

    return


if __name__ == "__main__":
    main()