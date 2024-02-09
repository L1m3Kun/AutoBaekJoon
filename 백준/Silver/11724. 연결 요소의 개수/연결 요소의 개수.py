# 11724 연결 요소의 개수
import sys
input = sys.stdin.readline

def find(x:int):
    tmp = x
    while tmp != root[tmp]:
        tmp = root[tmp]
    return root[tmp]    
    

def union(x1:int, x2:int):
    f1 = find(x1)
    f2 = find(x2)
    if f1 != f2:
        root[f2] = f1


def solution(N:int, M:int, root:list):
    for _ in range(M):
        u, v = map(int, input().split())
        union(u, v)
    cnt = set()
    for i in range(1, N+1):
        cnt.add(find(root[i]))
    print(len(cnt))
    

if __name__ == "__main__":
    N, M = map(int, input().split())
    root = [i for i in range(N+1)]
    solution(N, M, root)