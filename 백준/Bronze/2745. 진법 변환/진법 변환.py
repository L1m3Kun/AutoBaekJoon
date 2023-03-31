# 2745 진법 변환

num = {}
for i in range(10):
    num[str(i)] = i
for i in range(10, 36):
    num[chr(65+(i-10))] = i

N, B = input().strip().split()
ans = 0
for i in range(len(N)):
    ans += num[N[i]] * int(B)**(len(N)-1-i)
print(ans)
