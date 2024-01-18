# 1002 터렛
import sys
input = sys.stdin.readline


def solution(x1:int, y1:int, r1:int, x2:int, y2:int, r2:int):
    rad_sum = (r1+r2)**2
    rad_dis = (r1 - r2)**2
    distance= (x1-x2)**2 + (y1-y2)**2
    
    if distance == 0:
        return -1 if r1 == r2 else 0
    if rad_dis < distance < rad_sum:
        return 2
    if rad_sum == distance or rad_dis == distance:
        return 1
    return 0
    
    
        

if __name__ == "__main__":
    for _ in range(int(input())):
        print(solution(*list(map(int, input().split()))))