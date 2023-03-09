import sys
input = sys.stdin.readline


def coloring():
    num = 1
    while num<=V:
        if color_book[num]:
            num += 1
            continue
        stack = [num]
        color_book[num] = 1
        while stack:
            i = stack.pop()
            for j in graph[i]:
                if not color_book[j]:
                    color_book[j] = color_book[i] + 1
                    stack.append(j)
                if color_book[i]%2 == color_book[j]%2:
                    return 0
        num += 1
    return 1


for test_case in range(1, int(input())+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    # print(graph)
    for _ in range(E):
        spot, node = map(int, input().split())
        graph[spot].append(node)
        graph[node].append(spot)
    color = 0
    color_book = [0] * (V+1)
    if coloring():
        # print(color_book)
        print('YES')
    else:
        # print(color_book)
        print('NO')
    