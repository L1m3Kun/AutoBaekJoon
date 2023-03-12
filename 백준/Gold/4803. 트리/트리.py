import sys
# sys.stdin = open('Tree\input.txt', 'r')
input = sys.stdin.readline
test_case = 0
while True:
    n, m = map(int, input().strip().split())
    test_case += 1
    if n == 0 and m == 0:
        break
    else:
        graph = [[] for _ in range(n+1)]
        visited = []
        for i in range(m):
            spot, node = map(int, input().strip().split())
            graph[spot].append(node)
            graph[node].append(spot)
        cnt = 0
        for i in range(1, n+1):
            if i not in visited:
                root = [[] for _ in range(n+1)]
                stack = [i]
                graph_visited = [0] * (n+1)
                graph_visited[i] = 1
                while stack:
                    t = stack.pop()
                    if t not in visited:
                        visited.append(t)
                    for j in graph[t]:
                        if j not in root[t]:
                            root[j].append(t)
                        if not graph_visited[j]:
                            graph_visited[j] += 1
                            stack.append(j)
                        else:
                            graph_visited[j] += 1
                for k in range(1, n+1):
                    # if graph_visited[k] > 2:
                    #     break
                    if len(root[k])>1:
                        break
                else:
                    cnt += 1
        print(f'Case {test_case}:', end=' ')
        if cnt > 1:
            print(f'A forest of {cnt} trees.')
        elif cnt == 1:
            print('There is one tree.')
        else:
            print('No trees.')