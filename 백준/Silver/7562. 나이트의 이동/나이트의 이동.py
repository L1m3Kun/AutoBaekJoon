import sys
from collections import deque
input = sys.stdin.readline

direction = [       # 방향
    (-1, -2),
    (-2, -1),
    (-2, 1),
    (-1, 2),
    (1, 2),
    (2, 1),
    (2, -1),
    (1, -2)
]

for test_case in range(1, int(input())+1):
    I = int(input())
    knight = list(map(int, input().strip().split()))
    goal = list(map(int, input().strip().split()))
    min_cnt = I**2
    # BFS
    if knight[0] == goal[0] and knight[1] == goal[1]:
        print(0)
    else:
        queue = deque([(knight[0], knight[1])])
        visited = [[0] * I for _ in range(I)]
        # visited[knight[0]][knight[1]] = 0
        while queue:
            i, j = queue.popleft()
            if i == goal[0] and j == goal[1]:
                min_cnt = min(min_cnt, visited[i][j])
                break
                # continue
            elif visited[i][j] > min_cnt:
                continue
            else:
                for di, dj in direction:
                    ni = i + di
                    nj = j + dj
                    if 0<=ni<I and 0<=nj<I and not visited[ni][nj]:
                        queue.append((ni,nj))
                        visited[ni][nj] = visited[i][j] + 1
        # [print(*visited[i]) for i in range(I)]
        print(min_cnt)