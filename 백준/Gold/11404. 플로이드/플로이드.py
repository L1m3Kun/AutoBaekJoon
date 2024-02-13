# 11404 플로이드
import sys
input = sys.stdin.readline


def floyd_warshall(N:int, distance:list):
    for i in range(N): # 경유
        for j in range(N): # 시작
            for k in range(N): # 도착
                distance[j][k] = min(distance[j][k], distance[j][i] + distance[i][k])
    return distance

def solution():
    N = int(input())
    M = int(input())
    limit = 100_001*N
    distance = [[limit] * (N) for _ in range(N)]
    for i in range(N):
        distance[i][i] = 0 

    for _ in range(M):
        s, e, c = map(int, input().split())
        distance[s-1][e-1] = min(distance[s-1][e-1], c)

    ans = floyd_warshall(N, distance)
    for i in range(N):
        for j in range(N):
            if ans[i][j] == limit:
                print(0, end=" ")
            else:
                print(ans[i][j], end= " ")
        print()

if __name__ == "__main__":
    solution()