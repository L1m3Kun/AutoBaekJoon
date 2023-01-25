def average(num):
    return int(sum(num) / len(num))          # 평균

def center(num):
    num.sort()
    return num[len(num)//2]             # 중앙값

N = []
for _ in range(5):
    N.append(int(input()))
print(average(N))
print(center(N))