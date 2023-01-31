import sys
stack = []
for order in range(int(sys.stdin.readline())):
    order = list(sys.stdin.readline().strip().split())
    # print(order)
    # print(stack)
    if order[0] == 'push':
        # print(order[1])
        stack.append(int(order[1]))
    elif order[0] == 'pop':
        try:
            print(stack.pop(-1))
        except:
            print(-1)
    elif order[0] == 'size':
        print(len(stack))
    elif order[0] == 'empty':
        if len(stack) != 0:
            print(0)
        else:
            print(1)
    elif order[0] == 'top':
        try:
            print(stack[-1])
        except:
            print(-1)