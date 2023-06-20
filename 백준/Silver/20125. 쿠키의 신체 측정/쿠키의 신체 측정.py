# 20125 쿠키의 신체 측정
import sys
input = sys.stdin.readline

N = int(input())
plate = [input().strip() for _ in range(N)]
# [print(*plate[i])for i in range(N)]
def searchHeart():
    for i in range(N):
        for j in range(N):
            if plate[i][j] == "*":
                heart_i = i+1 if i+1 < N else i
                heart_j = j
                while heart_i < N:
                    if heart_j - 1 >=0 and heart_j <N and plate[heart_i][heart_j-1] == "*" and plate[heart_i][heart_j+1] == "*":
                        return (heart_i, heart_j)
                    else:
                        heart_i += 1

def length_of(heart):
    y, x = heart
    length = [0, 0, 0, 0, 0]
    # left_arm = right_arm = waist = left_leg = right_leg = 0
    for i in range(x+1):
        if plate[y][i] == "*":
            # left_arm = x - i - 1
            length[0] = x - i 
            break
    for i in range(N-1, x,-1):
        if plate[y][i] == "*":
            # right_arm = i - x + 1
            length[1] = i - x
            break
    for i in range(1,N):
        if plate[y+i][x] == "_":
            break
        else:
            length[2] += 1
    for i in range(1,N):
        # print(y+length[2]+i)
        if y+length[2]+i>=N or plate[y+length[2]+i][x-1] == "_":
            break
        else:
            length[3] += 1
    for i in range(1,N):
        if y+length[2]+i>=N or plate[y+length[2]+i][x+1] == "_":
            break
        else:
            length[4] += 1
    return length
heart = searchHeart()
print(heart[0] +1, heart[1]+1)
print(*length_of(heart))
        