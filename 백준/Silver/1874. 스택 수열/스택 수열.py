import sys

n = int(sys.stdin.readline())

stack_list = [int(sys.stdin.readline()) for _ in range(n)]
stack = [1]
result = ['+']
idx = 1
try:
    while len(stack_list) != 0:
        if stack:
            if stack[-1] == stack_list[0]:
                result.append('-')
                stack.pop(-1)
                stack_list.pop(0)
            elif stack[-1] < stack_list[0] or len(stack) == 0:
                for num in range(idx+1,stack_list[0]+1):
                    result.append('+')
                    stack.append(num)
                idx = stack_list[0]
            else:
                raise ValueError()
                break
        else:
            for num in range(idx+1,stack_list[0]+1):
                result.append('+')
                stack.append(num)
            idx = stack_list[0]
    print('\n'.join(result))
except:
    print('NO')