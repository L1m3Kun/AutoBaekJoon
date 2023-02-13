import sys
# stack 선언
stack = []
# 입력 받은 값만큼 반복문 돌림
for _ in range(int(sys.stdin.readline().strip())):
    # 숫자입력받기
    n = int(sys.stdin.readline().strip())
    # n이 0이 아니면 stack에 추가
    if n:
        stack.append(n)
    else:
    # 0이면 stack에 있는 마지막 숫자 빼기
        if stack:
            stack.pop()
print(sum(stack))