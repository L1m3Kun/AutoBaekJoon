# 1865 웜홀
import sys
input = sys.stdin.readline


def bellman_ford(N:int, M:int, graph:list):
    visited =[10_001*M] *(N+1)
    visited[1] = 0
    for i in range(N):
        for node in graph:
            s, e, t = node
            if visited[e] > visited[s] + t:
                visited[e] = visited[s] + t
                if i == N-1:
                    return "YES"
    return "NO"

def solution():
    N, M, W = map(int, input().split())
    graph = []
    for _ in range(M):
        s,e,t = map(int, input().split())
        graph.append(tuple([s,e,t]))
        graph.append(tuple([e,s,t]))
    for _ in range(W):
        s,e,t = map(int, input().split())
        graph.append(tuple([s,e,-t]))
    print(bellman_ford(N, M, graph))
    return


if __name__ == "__main__":
    for _ in range(int(input())):
        solution()