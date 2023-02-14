import sys

def solution():
    stack = []
    open_p = ['(', '[']
    close_p = [')', ']']
    for i in sentence:
        for j in i:
            if j in open_p:
                stack.append(j)
            elif j in close_p:
                if stack:
                    if open_p.index(stack[-1]) == close_p.index(j):
                        stack.pop()
                    else:
                        return 'no'
                else:
                    return 'no'
    if len(stack) == 0:
        return 'yes'
    else:
        return 'no'


while True:
    sentence = list(sys.stdin.readline())
    if sentence == ['.', '\n']:
        break
    else:
        print(solution())






