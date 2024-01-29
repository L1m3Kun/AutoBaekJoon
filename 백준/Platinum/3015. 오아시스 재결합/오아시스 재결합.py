# 3015 오아시스 재결합
import sys
input = sys.stdin.readline


def solution():
    stack = []
    cnt = 0
    for _ in range(int(input())):
        fan = int(input())
        
        while stack and fan > stack[-1][0]:
            cnt += stack.pop()[1]
        
        if stack:
            if fan == stack[-1][0]:
                cnt += stack[-1][1]
                if len(stack) > 1:
                    cnt += 1
                stack[-1][1] += 1
            else:
                stack.append([fan, 1])
                cnt += 1
        else:
            stack.append([fan, 1])


         
         
    print(cnt)

if __name__ == "__main__":
    solution()

    