import sys
input = sys.stdin.readline

lines = sorted(list(map(int, input().split())))
tw = lines[0]+lines[1]
print(tw+(tw-1 if lines[2] >= (tw-1) else lines[2]))