import sys


N, K = map(int, sys.stdin.readline().strip().split())
queue = list(range(1, N+1))
rear = count = 0
result = []
while True:
    if rear == len(queue)-1:
        rear = 0
    front = queue.pop(0)
    count+=1
    if count % K:
        rear += 1
        queue.append(front)
    else:
        rear -= 1
        result.append(front)
    if not queue:
        break
print(f'<{", ".join(map(str,result))}>')

