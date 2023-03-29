import sys
input = sys.stdin.readline

a, b, c, d, e, f = map(int, input().split())

y = (c * d - a * f) / (a*e - b*d)
x = (-e * c + b * f) / (a*e - b*d)
print(int(-x), int(-y))