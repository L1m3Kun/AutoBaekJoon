import sys

N = int(sys.stdin.readline())

people = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

frame_list = []
for i in range(N):
    frame = 1
    for j in range(N):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            frame += 1
    frame_list.append(frame)

print(*frame_list)
