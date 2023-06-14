import sys

N= int(sys.stdin.readline())
end_num = 0
count = 0
while True:
    end_num += 1
    if '666' in str(end_num):
        count += 1
        if count == N:
            break
print(end_num)
