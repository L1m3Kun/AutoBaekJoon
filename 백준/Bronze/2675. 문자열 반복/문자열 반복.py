import sys

def repeat_str(str):
    R = int(str[0])             # 입력받은 리스트에서 반복숫자 꺼내기
    total = ""                       
    for idx in str[1]:
        total = total + idx*R           # 반복해서 출력
    return total
        
T = int(sys.stdin.readline().strip())
for test_case in range(1,T+1):
    S = list(sys.stdin.readline().strip().split())
    print(repeat_str(S))