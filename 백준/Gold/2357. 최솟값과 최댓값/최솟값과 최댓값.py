# 2357 최솟값과 최댓값
import sys
input = sys.stdin.readline


def main():
    N, M = map(int, input().split())

    tree = [(0,0)] * (N*2)
    for i in range(N, 2*N):
        n = int(input())
        tree[i] = (n,n)
    # print(tree)

    for i in range(N-1,0,-1):
        tree[i] = (min(tree[(i<<1)+1][0],tree[i<<1][0]), max(tree[(i<<1)+1][1],tree[i<<1][1]))
    
    # print(tree)

    for _ in range(M):
        start, end = map(int, input().split())
        start, end = (start-1) + N, end + N
        result = [1_000_000_001, 0]
        while start < end:
            if start & 1:
                result = (min(result[0],tree[start][0]), max(result[1],tree[start][1]))
                start += 1

            if end & 1:
                end -= 1
                result = (min(result[0],tree[end][0]), max(result[1],tree[end][1]))
                
            start >>= 1
            end >>= 1
        print(*result)

    return


if __name__ == "__main__":
    main()