# 1725 히스토그램
import sys
input = sys.stdin.readline


def solution():
    N = int(input())
    stack = [[int(input()),1]]
    maxv = stack[0][0]
    for _ in range(N-1):
        height = int(input())
        
        c = 1
        while stack and stack[-1][0] > height:
            minv, cnt = stack.pop()
            c += cnt
            maxv = max(maxv, minv*(c-1))

        stack.append([height, c])

    else:
        while stack:
            minv, cnt = stack.pop()
            c += cnt
            maxv = max(maxv, minv*(c-1))
    print(maxv)
   
            
if __name__ == "__main__":
    solution()