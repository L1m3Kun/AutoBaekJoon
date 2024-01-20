# 9935 문자열 폭발
import sys
input = sys.stdin.readline


def solution(S:str, boom:str) -> str:
    stack = []
    len_b = len(boom)
    for i in range(len(S)):
        stack.append(S[i])
        if len(stack) >= len_b and stack[-len_b:] == list(boom):
            for _ in range(len_b):
                stack.pop()
    return "".join(stack) if stack else "FRULA"


if __name__ == "__main__":
    print(solution(input().strip(), input().strip()))