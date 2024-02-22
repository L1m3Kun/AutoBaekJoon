import sys
input = sys.stdin.readline


def solution():
    triangle = tuple([int(input()) for _ in range(3)])
    
    if sum(triangle) != 180:
        print("Error")
    elif triangle[0] == triangle[1] == triangle[2] == 60:
        print("Equilateral")
    elif triangle[0] == triangle[1] or triangle[1] == triangle[2] or triangle[0] == triangle[2]:
        print("Isosceles")
    else:
        print("Scalene")
        

if __name__ == "__main__":
    solution()