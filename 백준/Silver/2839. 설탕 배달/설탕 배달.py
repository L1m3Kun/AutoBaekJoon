import sys

N = int(sys.stdin.readline())
result = []

if N >=5:
    for i in range(N // 5):
        if (N - 5 * (N//5-i)) % 3 == 0:
            a = N//5 -i
            b = (N - 5 * (N//5-i)) // 3
            result.append(a+b)
        if not N % 3:
            result.append(N//3)
    else:
        if not result:
            result.append(-1)
else:
    if N % 3==0:
        result.append(N//3)
    else:
        result.append(-1)

print(min(result))
