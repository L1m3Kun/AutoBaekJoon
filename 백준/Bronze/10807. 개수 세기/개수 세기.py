n = int(input())
arr = list(map(int,input().split()))
v = int(input())
count=0
for i in arr:
    if v == i:
        count+=1
print(count)