# 11657 타임머신
import sys
input = sys.stdin.readline


def bellman_ford(N:int, nodes:list):
    distance = [[10_001*N,0] for _ in range(N+1)]
    distance[1][0] = 0

    for i in range(N):
        for node in nodes:
            s, e, c = node
            if distance[s][0] == 10_001 * N :
                continue
            if distance[e][0] > distance[s][0] + c:
                distance[e][0] = distance[s][0] + c
                distance[e][1] += 1
                if i == N-1:
                    return [-1]
    
    return list(map(lambda x:x[0], distance))
    


def solution():
    N, M = map(int, input().split())
    nodes = []
    for _ in range(M):
        A, B, C = map(int, input().split())
        nodes.append((A,B,C))
    ans = bellman_ford(N, nodes)
    if ans[0] == -1:
        print(-1)
    else:
        for i in range(2, N+1):
            if ans[i] == 10_001*N:
                print(-1)
            else:
                print(ans[i])
    


if __name__ == "__main__":
    solution()

