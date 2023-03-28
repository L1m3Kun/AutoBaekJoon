import sys
input = sys.stdin.readline

def solution(stack):
    if len(stack) == L:
        cnt = 0
        for i in moum:
            if i in stack:
                cnt += 1
        if 0 < cnt <= (L-2):
            print(''.join(stack))
        return
    for i in range(C):
        if arr[i] not in stack:
            if len(stack):
                if stack[-1] < arr[i]:
                    stack.append(arr[i])
                    solution(stack)
                    stack.pop()    
            else:
                stack.append(arr[i])
                solution(stack)
                stack.pop()
    return




L, C = map(int, input().split())
arr = sorted(list(input().strip().split()))
moum = ['a', 'e', 'i', 'o', 'u']
stack = []
solution(stack)