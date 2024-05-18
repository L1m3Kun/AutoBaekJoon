# 17471 게리맨더링
import sys
from collections import deque
input = sys.stdin.readline


def main():
    N = int(input())
    population = tuple(map(int,input().split()))
    graph = [[] for _ in range(N)]
    total_population = sum(population)
    total = 0
    for i in range(N):
        _, *near = map(int, input().split())
        total += _
        graph[i] = set(map(lambda x:x-1, near))

    if N == 2:
        print(abs(population[0]-population[1]))
        return
    
    stack = []
    visited = [0] * N
    # print(graph)

    def check(is_stack):
        if is_stack:
            que = deque([stack[0]])
            v = set([stack[0]])
            compare = set(stack)
        else:
            tmp = []
            for i in range(N):
                if i not in stack:
                    tmp.append(i)
                    

            que = deque([tmp[0]])
            v = set([tmp[0]])
            compare = set(tmp)

        while que:
            spot = que.popleft()

            for node in graph[spot]:
                if not (node in v) and node in compare:
                    v.add(node)
                    que.append(node)

        
        return 1 if v == compare else 0
        


    def bt(city, minv, men):
        
        if len(stack) > 1:
            if check(0) and check(1):
                minv = min(minv, abs(total_population-men*2))
        elif len(stack) == 1:
            if check(0):
                minv = min(minv, abs(total_population-men*2))
        
        
        if len(stack) == N//2:
            return minv



        for i in range(city+1, N):
            if not visited[i]:
                visited[i] = 1
                stack.append(i)
                minv = min(minv,bt(i, minv, (men+population[i])))
                visited[i] = 0
                stack.pop()
        
        return minv
    

    ans = bt(-1, 10000, 0)
    if ans == 10000:
        print(-1)
    else:
        print(ans)

    return


if __name__ == "__main__":
    main()