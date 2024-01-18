# 2531 회전초밥
import sys
from collections import deque, defaultdict
input = sys.stdin.readline

# def kindLen(lst, element):
    
#     return len(set(lst)) if element in lst else len(set(lst))+1

N, d, k, c = map(int, input().split())
sushies = [int(input()) for _ in range(N)]

kind = defaultdict(int)

i, j = 0, k
event_sushies = deque(sushies[0:k])
for idx in event_sushies:
    kind[idx] += 1
# max_kind = kindLen(event_sushies, c)
max_kind = len(kind.keys())
while i < N:
    poped = event_sushies.popleft()
    kind[poped] -= 1
    if not kind[poped]:
        kind.pop(poped)
    event_sushies.append(sushies[j])
    kind[sushies[j]] += 1
    if c in kind.keys():
        max_kind = max(max_kind, len(kind.keys()))
    else:
        max_kind = max(max_kind, len(kind.keys())+1)
#  print(i, j, "i와 j")
#  print(event_sushies, "event_")

  # max_kind = max(max_kind, kindLen(event_sushies, c))
    i += 1
    j = (j+1)%N

print(max_kind)
        