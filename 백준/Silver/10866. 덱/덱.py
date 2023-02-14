import sys

deque = []
for _ in range(int(sys.stdin.readline().strip())):
    order = list(sys.stdin.readline().strip().split())
    if order[0] == 'push_front':
        if deque:
            tmp = deque.copy()
            deque.clear()
            deque.append(order[1])
            deque += tmp
        else:
            deque.append(order[1])
    elif order[0] == 'push_back':
        deque.append(order[1])
    elif order[0] == 'pop_front':
        print(deque.pop(0)) if deque else print(-1)
    elif order[0] == 'pop_back':
        print(deque.pop()) if deque else print(-1)
    elif order[0] == 'size':
        print(len(deque))
    elif order[0] == 'empty':
        print(0) if deque else print(1)
    elif order[0] == 'front':
        print(deque[0]) if deque else print(-1)
    elif order[0] == 'back':
        print(deque[-1]) if deque else print(-1)
