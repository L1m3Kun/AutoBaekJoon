# 1725 히스토그램
import sys
input = sys.stdin.readline


def solution():
    while True:
        N, *arr = map(int, input().split())
        if N == 0:
            break
        stack = [[arr[0],1]]
        maxv = stack[0][0]
        for k in range(1, N):
            height = arr[k] 
        
            c = 1
            while stack and stack[-1][0] > height:
                minv, cnt = stack.pop()
                c += cnt
                maxv = max(maxv, minv*(c-1))

            stack.append([height, c])

        else:
            c=1
            while stack:
                minv, cnt = stack.pop()
                c += cnt
                maxv = max(maxv, minv*(c-1))
        print(maxv)
   
            
if __name__ == "__main__":
    solution()
    