import sys
que = []                            # queue 생성

def push_que(x):            
    que.append(x)                   # queue 삽입

def pop_que():
    if len(que) > 0:
        return que.pop(0)           # 첫번째 인자 빼기
    else: 
        return -1

def size_que():
    return len(que)                 # 길이

def empty_que():
    if len(que) == 0:
        return 1
    else:
        return 0

def front_que():
    if len(que) > 0:
        return que[0]
    else: 
        return -1

def back_que():
    if len(que) > 0:
        return que[-1]
    else: 
        return -1


N = int(sys.stdin.readline())

for _ in range(N):
    order = list(sys.stdin.readline().strip().split())
    if order[0] == 'push':
        push_que(order[1])
    elif order[0] == 'pop':
        print(pop_que())
    elif order[0] == 'size':
        print(size_que())
    elif order[0] == 'empty':
        print(empty_que())
    elif order[0] == 'front':
        print(front_que())
    elif order[0] == 'back':
        print(back_que())