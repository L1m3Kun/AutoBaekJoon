# 5052 전화번호 목록
import sys
input = sys.stdin.readline


def solution():
    N = int(input())
    snack_line = list(map(int, input().split()))
    line = []
    next = 1
    idx = 0
    while next <= N:
        if idx >= N:
            if line[-1] == next:
                next+= 1
                line.pop()
                continue
            else:
                break
        if snack_line[idx] == next:
            idx += 1
            next += 1
        elif line and line[-1] == next:
            line.pop()
            next += 1
        else:
            line.append(snack_line[idx])
            idx += 1
    if line:
        print("Sad")
    else:
        print("Nice")
        
    
    


if __name__ == "__main__":
    solution()