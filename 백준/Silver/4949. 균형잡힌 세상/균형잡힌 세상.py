import sys

def solution():
    stack = []  # stack
    # 괄호 확인용 리스트
    open_p = ['(', '[']
    close_p = [')', ']']
    for i in sentence:
        # 괄호가 open에 있을 때는 stack에 추가
        if i in open_p:
            stack.append(i)
        # close에 있을 때는 stack에 뭐가 있는지 보고 없으면 no
        elif i in close_p:
            if stack:
                # 있더라도 짝이 안맞으면 no
                if open_p.index(stack[-1]) == close_p.index(i):
                    stack.pop()
                else:
                    return 'no'
            else:
                return 'no'
    # stack에 있는 열린 괄호들이 짝이 다 맞으면 yes
    if len(stack) == 0:
        return 'yes'
    else:
        return 'no'


while True:
    sentence = list(sys.stdin.readline())
    # readline()으로 가져오기때문에 \n 기호가 포함되어있음
    if sentence == ['.', '\n']:
        break
    else:
        print(solution())
