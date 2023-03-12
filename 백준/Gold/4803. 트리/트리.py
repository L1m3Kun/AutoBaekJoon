import sys
# sys.stdin = open('Tree\input.txt', 'r')
input = sys.stdin.readline
test_case = 0
while True:     # 입력 받기
    n, m = map(int, input().strip().split())
    test_case += 1
    if n == 0 and m == 0:
        break
    else:
        # 그래프 만들기
        graph = [[] for _ in range(n+1)]
        visited = [0] * (n+1)
        for i in range(m):
            spot, node = map(int, input().strip().split())
            graph[spot].append(node)
            graph[node].append(spot)
        cnt = 0         # 트리 세기 용
        for i in range(1, n+1):
            if not visited[i]:
                root = [[] for _ in range(n+1)]     # 트리의 부모를 저장하여 부모가 둘 이상이면 그래프 아니면 트리
                stack = [i]
                visited[i] = 1
                while stack:
                    t = stack.pop()
                    for j in graph[t]:
                        if j not in root[t]:        # 부모 정점 저장
                            root[j].append(t)
                        if not visited[j]:
                            stack.append(j)
                            visited[j] += 1
                        else:
                            visited[j] += 1
                for k in range(1, n+1):
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